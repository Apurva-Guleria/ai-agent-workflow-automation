from app.workflow.loader import WorkflowLoader
from app.engine.registry import WorkflowRegistry


loader = WorkflowLoader("data/workflows.xlsx")

workflows = loader.load_workflows()

registry = WorkflowRegistry(workflows)

workflow = registry.get_workflow("WF001")

print("Workflow ID:", workflow["id"])
print("Workflow Name:", workflow["name"])
print("Trigger:", workflow["trigger"])