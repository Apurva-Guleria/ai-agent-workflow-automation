from app.workflow.loader import WorkflowLoader
from app.engine.registry import WorkflowRegistry
from app.agent.selector import WorkflowSelector
from app.engine.executor import WorkflowExecutor
from app.engine.tool_registry import ToolRegistry
from app.tools.llm_tool import LLMTool


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
loader = WorkflowLoader(str(BASE_DIR / "data" / "workflows.xlsx"))
workflows = loader.load_workflows()

# Workflow registry
registry = WorkflowRegistry(workflows)

# LLM
llm = LLMTool()

# AI workflow selector
selector = WorkflowSelector(registry, llm)

# Tool registry
tool_registry = ToolRegistry()

# Workflow executor
executor = WorkflowExecutor(
    registry,
    tool_registry
)


# User request
request = "Assign this urgent task to the best available developer."
print("User Request:", request)

# AI selects workflow
selection = selector.select_workflow(request)

print("\nAI Selection:")
print("Workflow:", selection["workflow_id"])
print("Reason:", selection["reason"])

workflow = registry.get_workflow(selection["workflow_id"])

print("\nTools Required from Excel:")
print(workflow["tools"])

# Execute selected workflow
result = executor.execute(
    selection["workflow_id"],
    request
)

print("\nFinal Result:")
print(result)