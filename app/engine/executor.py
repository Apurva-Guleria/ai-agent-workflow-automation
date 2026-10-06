class WorkflowExecutor:
    def __init__(self, registry, tool_registry):
        self.registry = registry
        self.tool_registry = tool_registry

    def execute(self, workflow_id, user_request=None):
        workflow = self.registry.get_workflow(workflow_id)

        if not workflow:
            raise ValueError(f"Workflow {workflow_id} not found")

        print(f"\nExecuting Workflow: {workflow['name']}")

        if user_request:
            print(f"User Request: {user_request}")

        tool_names = self.tool_registry.get_tools_for_workflow(
            workflow["tools"]
        )

        print("\nTools selected:")

        for tool_name in tool_names:
            print("-", tool_name)

        result = self.tool_registry.execute_workflow(
            workflow_id,
            user_request
        )

        result_status = (
            result.get("status", "success")
            if isinstance(result, dict)
            else "success"
        )

        return {
            "workflow_id": workflow["id"],
            "workflow_name": workflow["name"],
            "status": result_status,
            "result": result
        }