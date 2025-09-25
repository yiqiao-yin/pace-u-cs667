import os
import re
import json
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

import chainlit as cl
import anthropic
from mcp import ClientSession

# === Load environment variables ===
load_dotenv()
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY", "your-key-here")
claude = anthropic.AsyncAnthropic(api_key=anthropic_api_key)

# === SQLite Fake Table ===
df_fake = pd.DataFrame({
    "user_id": [1, 2, 3, 2],
    "user_name": ["Alice", "Bob", "Charlie", "Bob"],
    "transaction_id": [1, 2, 3, 4],
    "amount": [100.5, 200.0, 150.25, 300.0],
    "status": ["approved", "declined", "approved", "approved"]
})

engine = create_engine("sqlite://", echo=False)
table_name = "SAMPLE_TABLE_NAME"
df_fake.to_sql(table_name, con=engine, index=False, if_exists="replace")

# === System Prompt for Claude ===
SYSTEM_PROMPT = f"""
You are a SQL assistant. Only output a SELECT SQL query inside a markdown block.
Use the table  with the following schema:

- user_id (integer)
- user_name (string)
- transaction_id (integer)
- amount (float)
- status (string: 'approved', 'declined')

Only return syntactically correct SQL. Do not explain or describe the SQL.
"""

# === Extract SQL from Claude response ===
def extract_sql_from_markdown(text: str) -> str:
    match = re.search(r"", text, re.DOTALL | re.IGNORECASE)
    return " ".join(match.group(1).strip().split()) if match else ""

# === Run SQL query ===
def run_sql_query(sql: str) -> pd.DataFrame:
    try:
        with engine.connect() as conn:
            return pd.read_sql(text(sql), conn)
    except Exception as e:
        return pd.DataFrame({"error": [str(e)]})

# === Native Tool ===
@cl.step(type="tool")
async def query_sqlite(sql_query: str) -> str:
    df = run_sql_query(sql_query)
    if "error" in df.columns:
        return f"❌ SQL Error: {df['error'][0]}"
    return df.to_markdown(index=False)

# === Claude Stream LLM Call ===
async def call_claude(chat_messages):
    tools = cl.user_session.get("regular_tools", []) + sum(cl.user_session.get("mcp_tools", {}).values(), [])
    msg = cl.Message(content="")

    async with claude.messages.stream(
        model="claude-3-5-sonnet-20240620",
        system=SYSTEM_PROMPT,
        max_tokens=1024,
        messages=chat_messages,
        tools=tools,
    ) as stream:
        async for token in stream.text_stream:
            await msg.stream_token(token)
    await msg.send()

    return await stream.get_final_message()

# === Chainlit Lifecycle ===
@cl.on_chat_start
async def start_chat():
    cl.user_session.set("chat_messages", [])
    cl.user_session.set("regular_tools", [
        {
            "name": "query_sqlite",
            "description": "Run SQL query on sample SQLite table.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "sql_query": {"type": "string"}
                },
                "required": ["sql_query"]
            }
        }
    ])

@cl.on_message
async def on_message(msg: cl.Message):
    chat_messages = cl.user_session.get("chat_messages")
    chat_messages.append({"role": "user", "content": msg.content})

    response = await call_claude(chat_messages)

    while response.stop_reason == "tool_use":
        tool_use = next(b for b in response.content if b.type == "tool_use")
        result = await query_sqlite(**tool_use.input)
        chat_messages.extend([
            {"role": "assistant", "content": response.content},
            {
                "role": "user",
                "content": [{
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": result
                }]
            }
        ])
        response = await call_claude(chat_messages)

    final_response = next((b.text for b in response.content if hasattr(b, "text")), None)
    chat_messages.append({"role": "assistant", "content": final_response})

# === Optional MCP Connect ===
@cl.on_mcp_connect
async def on_mcp(connection, session: ClientSession):
    tools = await session.list_tools()
    mcp_tools = cl.user_session.get("mcp_tools", {})
    mcp_tools[connection.name] = [
        {
            "name": t.name,
            "description": t.description,
            "input_schema": t.inputSchema,
        } for t in tools.tools
    ]
    cl.user_session.set("mcp_tools", mcp_tools)