from app.tools.employee_task_tool import EmployeeTaskTool

tool = EmployeeTaskTool()

result = tool.assign_tasks(
    "data/employee_tasks.csv",
    "data/employees.csv"
)

for item in result:
    print(item)