import json


class WorkflowSelector:

    def __init__(self, registry, llm):
        self.registry = registry
        self.llm = llm

    def select_workflow(self, user_request):

        workflows = self.registry.get_all_workflows()

        workflow_context = []

        for workflow_id, workflow in workflows.items():
            workflow_context.append({
                "workflow_id": workflow_id,
                "name": workflow["name"],
                "trigger": workflow["trigger"],
                "inputs": workflow["inputs"],
                "expected_output": workflow["expected_output"]
            })

        prompt = f"""
You are an AI workflow selector.

Select the most appropriate workflow for the user's request.

Available workflows:
{json.dumps(workflow_context, indent=2)}

User request:
{user_request}

Return ONLY valid JSON in this format:

{{
    "workflow_id": "WF001",
    "reason": "short explanation"
}}

If no workflow matches, return:

{{
    "workflow_id": null,
    "reason": "No matching workflow found"
}}
"""

        response = self.llm.ask(prompt)

        try:
            result = json.loads(response)
            return result

        except json.JSONDecodeError:
            raise ValueError(
                f"LLM returned invalid JSON: {response}"
            )