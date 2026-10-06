from app.workflow.loader import WorkflowLoader
from app.engine.registry import WorkflowRegistry
from app.engine.executor import WorkflowExecutor


loader = WorkflowLoader("data/workflows.xlsx")

workflows = loader.load_workflows()

registry = WorkflowRegistry(workflows)

executor = WorkflowExecutor(registry)

result = executor.execute("WF001")

print("\nResult:")
print(result)