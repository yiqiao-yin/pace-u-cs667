# Table of Contents

- [Capstone Projects](#capstone-projects)
   - [Project 1: Credibility Score for Articles/Sources/References](#project-1-credibility-score-for-articlessourcesreferences)
     - [Concept Overview](#concept-overview)
     - [Approach to Scoring Credibility](#approach-to-scoring-credibility)
     - [Deliverable](#deliverable)
     - [Deliverable Deadline Breakdown](#deliverable-deadline-breakdown)
       - [Draft of the Python Function](#draft-of-the-python-function)
       - [Detailed Technique Report](#detailed-technique-report)
       - [Implementation into Live Applications](#implementation-into-live-applications)
   - [Project 2: TinyTroupe for Simulation](#project-2-tinytroupe-for-simulation)
     - [Concept Overview](#concept-overview-1)
     - [Approach to Simulating Feedback](#approach-to-simulating-feedback)
     - [Deliverable](#deliverable-1)
     - [Deliverable Deadline Breakdown](#deliverable-deadline-breakdown-1)
       - [Draft of the App](#draft-of-the-app)
       - [Beta Version and Technical Report](#beta-version-and-technical-report)
       - [Final Delivery of Container-Ready App](#final-delivery-of-container-ready-app)

# Capstone Projects

Please see the following projects. You must attempt the following submissions. Please read it carefully:

- Project 1 Submissions:
  - Feb. 8th: [Draft of the Python Function](#draft-of-the-python-function)
  - Feb. 22nd: [Detailed Technique Report](#detailed-technique-report)
  - Mar. 31st: [Implementation into Live Applications](#implementation-into-live-applications)
- Project 2 Submissions:
  - Mar. 15th: [Draft of the App](#draft-of-the-app)
  - Mar. 29th: [Beta Version and Technical Report](#beta-version-and-technical-report)
  - Apr. 5th: [Final Delivery of Container-Ready App](#final-delivery-of-container-ready-app)
- Project 3 Submission:
  - Apr. 30th: You must make one submission to deliver what you worked on for a project of your choice. You must choose at least one project [here](./extra_proj.md)

You can pass the class with successful submissions of the above deliverables. All deliverables will be submitted using [this link](https://airtable.com/appBjNPgdot15ZqO7/pagKL7hfbTouEflS9/form).

Please take these submissions seriously.

## Project 1: Credibility Score for Articles/Sources/References

![graph](./pics/12_capstone_01.png)

### Concept Overview
[Go back to TOC](#table-of-contents)

The objective is to assess the credibility of articles, sources, or references through a credibility score. This proof of concept is grounded in the Retrieval-Augmented Generation (RAG) algorithm. The use case involves:

- **Chatbot Integration**: Initially, we have a chatbot that employs the RAG algorithm for document-specific Q&A tasks.
- **Resource Aggregation**: RAG provides responses drawing from numerous resources.

The challenge is to understand and evaluate the credibility of these resources through a scoring mechanism.

### Approach to Scoring Credibility
[Go back to TOC](#table-of-contents)

1. **Machine Learning-Based**: Utilize machine learning techniques to rate sources by analyzing features derived from those sources.
2. **Rule-Based**: Define specific rules or heuristics to assess credibility.
3. **Hybrid Approach**: Combine both ML and rule-based methods for a comprehensive evaluation.
4. **Innovative Solutions**: Consider any other creative solutions that enhance credibility assessment beyond the traditional methods.

### Deliverable
[Go back to TOC](#table-of-contents)

The deliverable includes the implementation of a feature within the chatbot to display a credibility score alongside source references. This feature will involve:

- **Python Function**: A function designed to evaluate the URL of each reference.
  - **Input Argument**: The URL of the reference.
  - **Output**: A JSON object containing:
    ```json
    {
      "score": float,
      "explanation": string
    }
    ```
  - **Example Output**:
    ```json
    {"score": 0.90, "explanation": "This source is considered credible based on its citation count and author credentials."}
    ```

### Deliverable Deadline Breakdown
[Go back to TOC](#table-of-contents)

#### Draft of the Python Function
[Go back to TOC](#table-of-contents)

- **Objective**: Develop a preliminary version of the Python function that evaluates the URL of each reference.
- **Deliverables**:
  - A working draft of the function with basic functionality to return a JSON object containing:
    ```json
    {
      "score": float,
      "explanation": string
    }
    ```
  - Initial testing to validate input/output handling.

#### Detailed Technique Report
[Go back to TOC](#table-of-contents)

- **Objective**: Provide an in-depth analysis and report on the algorithmic approach and scientific research supporting the credibility scoring.
- **Deliverables**:
  - A comprehensive report covering:
    - The underlying algorithm used and its rationale.
    - Literature review of existing models and techniques for credibility assessment.
    - Justification of chosen methodologies, including both ML-based and rule-based approaches if applicable.
  - Documentation to guide future iterations and refinements.

#### Implementation into Live Applications
[Go back to TOC](#table-of-contents)

- **Objective**: Integrate the finalized Python function into live applications and ensure seamless operation with the chatbot.
- **Deliverables**:
  - Full implementation of the credibility scoring feature within the chatbot platform.
  - Testing and validation to ensure correct functionality and user interaction.
  - Integration support using a provided application template to streamline the process.

## Project 2: TinyTroupe for Simulation

![graph](./pics/12_capstone_02.png)

### Concept Overview
[Go back to TOC](#table-of-contents)

This project aims to demonstrate the use of simulation to generate feedback for features based on customer personas. For example, a company introducing a new button or feature in their iOS app must survey beta customers from targeted demographics to gather feedback. However, this traditional process is expensive and time-consuming due to the need to pay contractors and incentivize participants with rewards.

This project proposes an **AI-first solution** to simulate user feedback for features by modeling different customer personas. Recommended package: [TinyTroup](https://github.com/microsoft/TinyTroupe)

### Approach to Simulating Feedback
[Go back to TOC](#table-of-contents)

1. **Persona-Based Simulation**: Develop an AI model that generates realistic feedback based on predefined personas, such as tech-savvy users or casual users.
2. **Feature-Driven Inputs**: Allow the app to take feature descriptions as input and output persona-specific feedback.
3. **User Feedback Scenarios**: Simulate common scenarios such as beta feature rollouts or user onboarding.
4. **Feedback Analysis**: Aggregate the feedback to draw conclusions about user preferences, feature acceptance, and potential issues.

### Deliverable
[Go back to TOC](#table-of-contents)

The deliverable for this project is an interactive app built using **Streamlit** or **Gradio** that can simulate user conversations and display feedback for a given feature and persona. 

The app will include:

- **Input Fields**: To specify the feature description and persona type.
- **Output Display**: A conversational output simulating feedback based on the persona's characteristics.
- **Functionality**: A user-friendly interface that allows users to test various features and personas.

### Deliverable Deadline Breakdown
[Go back to TOC](#table-of-contents)

#### Draft of the App
[Go back to TOC](#table-of-contents)

- **Objective**: Develop an initial draft of the app showcasing the basic structure and persona-based feedback generation.
- **Deliverables**:
  - A minimal viable product (MVP) with a basic UI to input features and personas.
  - Initial persona simulation results.
  - Feedback from the instructor for refinement.

#### Beta Version and Technical Report
[Go back to TOC](#table-of-contents)

- **Objective**: Complete the bulk of the app development and submit a technical report.
- **Deliverables**:
  - A beta version of the app with more refined personas and improved feedback outputs.
  - A detailed technical report covering:
    - The simulation algorithm used.
    - Persona definition and creation process.
    - Use cases and examples.
  - Feedback from a second round of instructor review.

#### Final Delivery of Container-Ready App
[Go back to TOC](#table-of-contents)

- **Objective**: Deliver a fully functional app ready for deployment.
- **Deliverables**:
  - A container-ready app that can be deployed via Docker or cloud services.
  - Finalized persona database with diverse customer profiles.
  - Integration and deployment documentation.
  - End-to-end testing and validation of app functionality.

By implementing this simulation app, the project demonstrates how AI can streamline feature feedback collection, reducing costs and accelerating the go-to-market strategy. The result is a scalable, efficient solution for user feedback analysis.
