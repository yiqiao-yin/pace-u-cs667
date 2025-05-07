# Table of Contents

- [Capstone Projects](#capstone-projects)
  - [Project 1: Credibility Score for Articles/Sources/References](#project-1-credibility-score-for-articlessourcesreferences)
    - [Concept Overview](#concept-overview)
    - [Approach to Scoring Credibility](#approach-to-scoring-credibility)
    - [Deliverable](#deliverable)
    - [Milestone Breakdown](#milestone-breakdown)
      - [Draft of the Python Function](#draft-of-the-python-function)
      - [Detailed Technique Report](#detailed-technique-report)
      - [Implementation into Live Applications](#implementation-into-live-applications)
  - [Project 2: TinyTroupe for Simulation](#project-2-tinytroupe-for-simulation)
    - [Concept Overview](#concept-overview-1)
    - [Approach to Simulating Feedback](#approach-to-simulating-feedback)
    - [Deliverable](#deliverable-1)
    - [Milestone Breakdown](#milestone-breakdown-1)
      - [Understanding of Agentic Framework](#understanding-of-agentic-framework)
      - [Draft App and Technical Report](#draft-app-and-technical-report)
      - [Final Delivery of Container-Ready App](#final-delivery-of-container-ready-app)

# Capstone Projects

Below are two core capstone projects designed to deepen your understanding of real-world data science and AI-first solutions. Each project is broken into clear milestones. You are encouraged to attempt all milestones, but can adapt the scope depending on your background and interests.

You may also optionally choose a project of your own or from an external list of industry-inspired ideas for additional experience. These optional projects provide flexibility and are ideal for showcasing initiative and creativity.

All project deliverables will be submitted through a centralized course form or portal. Further instructions will be shared during class.

---

## Project 1: Credibility Score for Articles/Sources/References

![graph](./pics/12_capstone_01.png)

### Concept Overview

This project focuses on developing a system to assess the **credibility of articles, sources, or references**. The goal is to integrate a **credibility scoring mechanism** into a chatbot or data pipeline, enhancing transparency in information retrieval and generation.

Key motivations:

- **Chatbot Integration**: Evaluate the reliability of sources used by RAG (Retrieval-Augmented Generation) systems.
- **Resource Aggregation**: Automatically assess multiple documents and flag those with questionable trustworthiness.

### Approach to Scoring Credibility

1. **Machine Learning-Based**: Use features such as citation count, source reputation, publication frequency, and authorship for training a credibility classifier.
2. **Rule-Based**: Create heuristic checks for known sources, domains, or linguistic patterns.
3. **Hybrid Strategy**: Combine ML-based classifiers with rule-based filters for robustness.
4. **Creative Enhancements**: Propose additional layers (e.g., community voting, citation web graphing) for extended evaluations.

### Deliverable

Implement a function to output a credibility score and explanation for any given URL or textual reference. This function should be usable in various systems (chatbots, dashboards, or data pipelines).

- **Python Function Specification**:
  - **Input**: A URL or reference string.
  - **Output**:
    ```json
    {
      "score": float,
      "explanation": string
    }
    ```

### Milestone Breakdown

#### Draft of the Python Function

- **Goal**: Create a preliminary function that returns a credibility score with a short explanation.
- **Notes**: Focus on input validation and structuring outputs. This function does not need to be perfect—start simple.

#### Detailed Technique Report

- **Goal**: Write a clear, technical document outlining your approach to credibility scoring.
- **Suggested Topics**:
  - Algorithm/methodology used.
  - Literature review of related credibility assessment models.
  - Justification for chosen model or rules.
  - Future enhancements or open questions.

#### Implementation into Live Applications

- **Goal**: Deploy your function into a working prototype such as a chatbot or evaluation tool.
- **Examples**:
  - Streamlit or Flask dashboard showing score per reference.
  - API integration with document Q&A tool.
  - Optional user interface with real-time scoring.

---

## Project 2: TinyTroupe for Simulation

![graph](./pics/12_capstone_02.png)

### Concept Overview

This project proposes an **AI-first solution for simulating user feedback** using agentic personas. Traditional feedback collection (focus groups, A/B testing) is slow and costly. Instead, simulate feedback from diverse personas to test features quickly.

You’ll use the **TinyTroupe** framework, or build your own agent simulator, to generate realistic user feedback across different demographics.

### Approach to Simulating Feedback

1. **Persona Modeling**: Build out realistic user types (e.g., student, elderly, power user, casual user).
2. **Feature-Driven Simulation**: Input a new app feature and generate persona-specific feedback.
3. **Interactive Scenarios**: Model situations like onboarding, feature updates, or support tickets.
4. **Feedback Insights**: Analyze simulated data to drive product decisions or usability redesigns.

### Deliverable

Develop a feedback simulator web app using **Streamlit** or **Gradio**. Users should be able to input a new feature and select one or more personas to generate and display simulated feedback.

Key features to include:

- Dynamic inputs (feature description, persona profile)
- Output of realistic simulated conversations or summary feedback
- Optional: Add sentiment analysis or tagging of feedback themes

### Milestone Breakdown

#### Understanding of Agentic Framework

- **Goal**: Read and document foundational concepts behind simulation agents and persona modeling.
- **Deliverable**: A summary in Markdown or PDF outlining:
  - Key definitions and terminology
  - How agentic personas function in simulation
  - Relationship to generative models (e.g., LLMs)

#### Draft App and Technical Report

- **Goal**: Build a working draft of the app with basic persona selection and feedback generation.
- **Report Contents**:
  - App architecture and libraries used
  - Persona creation method
  - Sample use cases and scenarios

#### Final Delivery of Container-Ready App

- **Goal**: Deliver a polished, ready-to-deploy version of your app.
- **Include**:
  - Docker or cloud-ready packaging
  - Final set of personas and test cases
  - Documentation for deployment and usage
  - Usability validation or testing results

---

These projects are designed to help you practice building **AI-first** systems and gain fluency in **applied data science workflows**. You are encouraged to iterate, be creative, and apply your knowledge to tackle problems that matter.
