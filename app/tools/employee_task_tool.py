import pandas as pd


class EmployeeTaskTool:

    def assign_tasks(self, tasks_file, employees_file):
        tasks = pd.read_csv(tasks_file)
        employees = pd.read_csv(employees_file)

        assignments = []

        for _, task in tasks.iterrows():

            required_skill = task["required_skill"]
            priority = task["priority"]

            candidates = []

            for _, employee in employees.iterrows():

                if employee["availability"] != "Available":
                    continue

                employee_skills = [
                    skill.strip().lower()
                    for skill in employee["skills"].split("|")
                ]

                if required_skill.lower() in employee_skills:

                    score = 1

                    if priority == "High":
                        score += 2
                    elif priority == "Medium":
                        score += 1

                    candidates.append({
                        "employee_id": employee["employee_id"],
                        "employee_name": employee["employee_name"],
                        "score": score
                    })

            if candidates:
                candidates.sort(
                    key=lambda x: x["score"],
                    reverse=True
                )

                best_employee = candidates[0]

                assignments.append({
                    "task_id": task["task_id"],
                    "task_name": task["task_name"],
                    "assigned_employee": best_employee["employee_name"],
                    "employee_id": best_employee["employee_id"],
                    "priority": priority,
                    "score": best_employee["score"]
                })

            else:
                assignments.append({
                    "task_id": task["task_id"],
                    "task_name": task["task_name"],
                    "assigned_employee": None,
                    "employee_id": None,
                    "priority": priority,
                    "score": 0
                })

        return assignments