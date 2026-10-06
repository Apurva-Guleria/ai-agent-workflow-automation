from app.workflow.loader import WorkflowLoader
from app.engine.tool_registry import ToolRegistry


loader = WorkflowLoader("data/workflows.xlsx")
workflows = loader.load_workflows()

registry = ToolRegistry()

workflow = workflows["WF001"]

tools = registry.get_tools_for_workflow(
    workflow["tools"]
)

print("Workflow:", workflow["name"])
print("Tools required:", workflow["tools"])

print("\nSelected tools:")

for tool in tools:
    print("-", type(tool).__name__)