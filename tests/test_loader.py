from app.workflow.loader import WorkflowLoader


loader = WorkflowLoader("data/workflows.xlsx")

workflows = loader.load_workflows()

for workflow_id, workflow in workflows.items():
    print(workflow_id, "->", workflow["name"])