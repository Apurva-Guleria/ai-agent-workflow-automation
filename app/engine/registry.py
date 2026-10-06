class WorkflowRegistry:

    def __init__(self, workflows):
        self.workflows = workflows

    def get_workflow(self, workflow_id):
        return self.workflows.get(workflow_id)

    def get_all_workflows(self):
        return self.workflows