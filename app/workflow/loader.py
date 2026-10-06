import pandas as pd


class WorkflowLoader:

    def __init__(self, excel_path):
        self.excel_path = excel_path

    def load_workflows(self):
        df = pd.read_excel(
            self.excel_path,
            sheet_name="Workflows"
        )

        workflows = {}

        for _, row in df.iterrows():
            workflows[row["Workflow_ID"]] = {
                "id": row["Workflow_ID"],
                "name": row["Workflow_Name"],
                "trigger": row["Trigger"],
                "inputs": row["Inputs"],
                "steps": row["Steps"],
                "decision_logic": row["Decision_Logic"],
                "tools": row["Tools_Required"],
                "expected_output": row["Expected_Output"]
            }

        return workflows