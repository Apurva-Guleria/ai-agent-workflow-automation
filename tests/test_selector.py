from app.workflow.loader import WorkflowLoader
from app.engine.registry import WorkflowRegistry
from app.agent.selector import WorkflowSelector
from app.tools.llm_tool import LLMTool


loader = WorkflowLoader("data/workflows.xlsx")
workflows = loader.load_workflows()

registry = WorkflowRegistry(workflows)

llm = LLMTool()

selector = WorkflowSelector(registry, llm)


request = "Which products need restocking?"

result = selector.select_workflow(request)

print("\nUser Request:", request)
print("Selected Workflow:", result["workflow_id"])
print("Reason:", result["reason"])