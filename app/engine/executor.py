import re


class WorkflowExecutor:

    def __init__(self, registry, tool_registry):
        self.registry = registry
        self.tool_registry = tool_registry

    def execute(self, workflow_id, user_request=None):

        workflow = self.registry.get_workflow(workflow_id)

        if not workflow:
            raise ValueError(
                f"Workflow {workflow_id} not found"
            )

        print(f"\nExecuting Workflow: {workflow['name']}")

        if user_request:
            print(f"User Request: {user_request}")

        # ---------------------------------------------------------
        # Display workflow steps from Excel
        # ---------------------------------------------------------

        raw_steps = str(workflow.get("steps", ""))

        steps = [
            step.strip()
            for step in re.split(r"→|;|\n", raw_steps)
            if step.strip()
        ]

        print("\nSteps Executed:")

        for index, step in enumerate(steps, start=1):
            print(f"{index}. {step}")

        # ---------------------------------------------------------
        # Select required tools
        # ---------------------------------------------------------

        tool_names = self.tool_registry.get_tools_for_workflow(
            workflow["tools"]
        )

        print("\nTools selected:")

        for tool_name in tool_names:
            print("-", tool_name)

        # ---------------------------------------------------------
        # Execute workflow
        # ---------------------------------------------------------

        result = self.tool_registry.execute_workflow(
            workflow_id,
            user_request
        )

        # ---------------------------------------------------------
        # Determine execution status
        # ---------------------------------------------------------

        result_status = (
            result.get("status", "success")
            if isinstance(result, dict)
            else "success"
        )

        # ---------------------------------------------------------
        # Return final result
        # ---------------------------------------------------------

        return {
            "workflow_id": workflow["id"],
            "workflow_name": workflow["name"],
            "status": result_status,
            "result": result
        }