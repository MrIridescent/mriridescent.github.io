# Agent Cards: 2026 Agentic Mesh Ecosystem

## 1. **Researcher Agent**
- **Role**: Domain Exploration & Data Retrieval
- **Capabilities**:
    - **Query Knowledge**: Accessing MOCK_DB via MCP.
    - **Summarization**: Distilling long-form reports into actionable snippets.
- **MCP Tools**: `query_research`.
- **Primary Goal**: Provide high-fidelity context for the **Planner Agent**.

## 2. **Planner Agent**
- **Role**: Task Decomposition & Strategic Orchestration
- **Capabilities**:
    - **Reasoning**: Breaks down complex user requests into discrete tasks.
    - **Decision Making**: Decides which **Executor Agent** is best for a specific task.
- **MCP Tools**: `get_project_status`.
- **Primary Goal**: Create a step-by-step execution roadmap for the **Executor Agent**.

## 3. **Executor Agent**
- **Role**: Action Execution & System Interaction
- **Capabilities**:
    - **Task Execution**: Directly interacting with internal tools to perform work.
    - **Error Handling**: Identifying failures and reporting back to the **Planner Agent**.
- **MCP Tools**: `execute_task`.
- **Primary Goal**: Complete tasks and provide verifiable proof of work (MTTR reduction focus).

## 4. **Compliance Agent (Audit)**
- **Role**: Verification & Safety Guardrails
- **Capabilities**:
    - **Validation**: Ensures actions are logically sound and follow 2026 safety standards.
    - **Audit Trails**: Logs all interactions for post-deployment reviews.
- **Primary Goal**: Maintain 100% adherence to **Neuro-Symbolic** "Truth" models.
