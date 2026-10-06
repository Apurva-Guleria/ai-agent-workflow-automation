# AI Agent Workflow Automation

An AI-powered workflow automation system that reads workflow definitions from Excel, uses an LLM to select the appropriate workflow based on a user's request, and executes the selected workflow using reusable tools and deterministic business logic.

The system is designed as a reusable and scalable architecture instead of creating a separate chatbot for each workflow.

## Features

- Excel-based workflow definitions
- AI/LLM-based workflow selection
- Reusable workflow executor
- Centralized tool registry
- CSV/Excel data processing
- LLM-powered content generation
- Rule-based classification and decision logic
- Similarity-based duplicate detection
- Order lookup and error handling
- Dynamic user request handling
- Workflow performance reporting
- Scalable architecture for adding new workflows

## Architecture

```text
User Request
     ↓
AI Workflow Selector (LLM)
     ↓
Workflow Registry
     ↓
Generic Workflow Executor
     ↓
Tool Registry
     ↓
Reusable Tools
     ↓
Final Result
```

## Technology Stack

- Python
- Pandas
- OpenPyXL
- LangChain
- Groq LLM
- python-dotenv
- CSV/Excel-based data processing

> Note: The current implementation uses LangChain with Groq for LLM interaction. LangGraph is not required for the current execution flow.

## Workflow Definitions

The system currently supports the following workflows:

| ID | Workflow | Description |
|---|---|---|
| WF001 | Inventory Restock Check | Identifies products below minimum stock and calculates reorder quantity |
| WF002 | Product Price Validation | Finds products where vendor price differs beyond a threshold |
| WF003 | Vendor File Processing | Validates vendor CSV data and reports invalid rows |
| WF004 | Product Description Generator | Generates product descriptions using an LLM |
| WF005 | Customer Order Status | Looks up order status using a dynamic order ID |
| WF006 | Duplicate Product Detection | Detects similar product names using similarity scoring |
| WF007 | Marketing Campaign Brief | Generates structured campaign briefs using an LLM |
| WF008 | SEO Keyword Classification | Classifies keywords and recommends an SEO action |
| WF009 | Employee Task Assignment | Assigns tasks based on skills, availability and priority |
| WF010 | Workflow Performance Report | Calculates workflow execution and failure metrics |

## Example Requests

### Inventory Restock

```text
Which products need restocking?
```

### Price Validation

```text
Find products where vendor price differs by more than 10%.
```

### Vendor Processing

```text
Process this vendor spreadsheet and show invalid rows.
```

### Product Description

```text
Generate product descriptions for these products.
```

### Order Status

```text
What is the status of order ORD002?
```

### Duplicate Detection

```text
Find duplicate products.
```

### Marketing Campaign

```text
Create a marketing campaign brief.
```

### SEO Classification

```text
Classify these SEO keywords and recommend actions.
```

### Employee Assignment

```text
Assign employees to these tasks based on skills and availability.
```

### Performance Report

```text
Which workflows are failing most often?
```

## How the System Works

### 1. Excel Workflow Loading

The `WorkflowLoader` reads the `Workflows` sheet from the Excel file.

Each workflow contains information such as:

- Workflow ID
- Workflow Name
- Trigger
- Inputs
- Steps
- Decision Logic
- Required Tools
- Expected Output

The Excel file acts as the source of workflow definitions.

### 2. AI Workflow Selection

The user's natural-language request is sent to the LLM along with the available workflow definitions.

The LLM selects the most appropriate workflow and returns a structured response containing:

- Workflow ID
- Reason for selection

Example:

```text
User Request:
Which products need restocking?

AI Selection:
Workflow: WF001
Reason: The request matches the inventory restock workflow.
```

### 3. Workflow Execution

After selecting a workflow, the `WorkflowExecutor` loads the corresponding workflow definition and sends execution to the centralized `ToolRegistry`.

The executor handles the common workflow execution flow while individual tools handle specific business operations.

### 4. Tool Registry

The `ToolRegistry` provides reusable tools such as:

- CSV reader
- Calculator
- Inventory processing
- Price validation
- Vendor file validation
- Order lookup
- Similarity detection
- Marketing campaign generation
- SEO classification
- Employee task assignment
- Performance reporting

This allows multiple workflows to use reusable components instead of creating separate applications for each workflow.

## LLM vs Deterministic Logic

The system intentionally separates LLM-based tasks from deterministic business logic.

### LLM Responsibilities

The LLM is used for:

- Understanding natural-language user requests
- Selecting the appropriate workflow
- Generating product descriptions
- Generating marketing campaign briefs

### Python Responsibilities

Python handles deterministic operations such as:

- Calculations
- Threshold comparisons
- CSV processing
- File validation
- Order lookup
- Similarity scoring
- Keyword classification
- Employee ranking
- Performance metrics

This separation improves reliability and makes business rules easier to test.

## Error Handling

The system handles common errors including:

- Invalid workflow selection
- Invalid LLM JSON response
- Missing required columns
- Invalid vendor data
- Missing order ID
- Unknown order ID
- Invalid calculations
- Empty datasets

Example:

```text
User Request:
What is the status of order ORD999?

Result:
Order ORD999 was not found.
```

## Scalability

The architecture is designed to support additional workflows without creating a separate chatbot for every workflow.

Workflow definitions are loaded from Excel and execution is handled through reusable components:

```text
Excel Workflow Definitions
          ↓
Workflow Loader
          ↓
Workflow Registry
          ↓
LLM Workflow Selector
          ↓
Generic Workflow Executor
          ↓
Tool Registry
          ↓
Reusable Tools
```

For an additional workflow such as `WF011`, the same architecture can be extended by adding its workflow definition and connecting the required reusable execution/tool logic.

The core selector and executor do not need to be rewritten as separate applications.

## Project Structure

```text
ai-agent-workflow-automation/
│
├── app/
│   ├── agent/
│   │   ├── agent.py
│   │   └── selector.py
│   │
│   ├── engine/
│   │   ├── executor.py
│   │   ├── registry.py
│   │   └── tool_registry.py
│   │
│   ├── tools/
│   │   ├── calculator.py
│   │   ├── csv_tool.py
│   │   ├── inventory_tool.py
│   │   ├── price_validation_tool.py
│   │   ├── vendor_file_tool.py
│   │   ├── product_description_tool.py
│   │   ├── order_status_tool.py
│   │   ├── similarity.py
│   │   ├── duplicate_product_tool.py
│   │   ├── marketing_campaign_tool.py
│   │   ├── seo_keyword_tool.py
│   │   ├── employee_task_tool.py
│   │   └── performance_report_tool.py
│   │
│   ├── workflow/
│   │   └── loader.py
│   │
│   └── main.py
│
├── data/
│   ├── workflows.xlsx
│   ├── inventory.csv
│   ├── products.csv
│   ├── vendor_data.csv
│   ├── product_description_input.csv
│   ├── orders.csv
│   ├── duplicate_products.csv
│   ├── marketing_campaign_input.csv
│   ├── seo_keywords.csv
│   ├── employee_tasks.csv
│   ├── employees.csv
│   └── execution_logs.csv
│
├── tests/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup & Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ai-agent-workflow-automation
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

The `.env` file contains the API key and should not be committed to GitHub.

A `.env.example` file is included as a template.

## Running the Project

The complete workflow can be tested using:

```bash
python test_agent_flow.py
```

The execution flow is:

```text
User Request
     ↓
LLM Workflow Selection
     ↓
Selected Workflow
     ↓
Required Tools
     ↓
Workflow Execution
     ↓
Final Result
```

## Testing Examples

### WF001

```text
Request:
Which products need restocking?

Expected:
WF001 is selected and low-stock products with reorder quantities are returned.
```

### WF002

```text
Request:
Find products where vendor price differs by more than 10%.

Expected:
WF002 is selected and products exceeding the threshold are returned.
```

### WF003

```text
Request:
Process this vendor spreadsheet and show invalid rows.

Expected:
WF003 is selected and invalid vendor rows with validation errors are returned.
```

### WF005

```text
Request:
What is the status of order ORD002?

Expected:
WF005 is selected and the order details are returned.
```

### WF006

```text
Request:
Find duplicate products.

Expected:
WF006 is selected and similar product pairs with similarity scores are returned.
```

### WF010

```text
Request:
Which workflows are failing most often?

Expected:
WF010 is selected and workflow failure metrics are returned.
```

## Design Decisions

### Excel as Workflow Source

The provided Excel file is treated as the source of workflow definitions.

This keeps workflow metadata separate from the application code.

### LLM + Deterministic Processing

The LLM is used for natural-language understanding and content generation.

Deterministic Python logic handles calculations, validation, ranking, comparisons and metrics.

### Centralized Tool Registry

Reusable tools are registered centrally and can be used by different workflows.

### Separation of Concerns

The application separates:

- Workflow loading
- Workflow selection
- Workflow registration
- Workflow execution
- Tool execution
- Data processing

This makes the system easier to test and extend.

## Assumptions

- CSV files are used as simulated data sources for the assessment.
- The order lookup represents a simulated database/API-style lookup using local data.
- The provided Excel file is treated as the workflow configuration source.
- External production APIs are not required for the assessment.
- LLM-generated content is constrained through prompts and provided input data.

## Security

- API keys are stored in environment variables.
- `.env` is excluded through `.gitignore`.
- `.env.example` contains only a placeholder API key.
- No secret credentials are included in the repository.

## Future Improvements

Possible production-level improvements include:

- Real database integration
- Real external API integrations
- LangGraph-based stateful orchestration
- Persistent workflow execution history
- Authentication and authorization
- Async workflow execution
- Workflow versioning
- Monitoring dashboard
- Automated workflow validation
- Additional workflow types

## Conclusion

This project demonstrates a reusable AI workflow automation architecture where an LLM understands a user's request, selects the appropriate workflow, and the system executes that workflow using reusable tools and deterministic Python logic.

The architecture is designed to scale beyond the initial 10 workflows while keeping workflow definitions, workflow execution and reusable tools separated.