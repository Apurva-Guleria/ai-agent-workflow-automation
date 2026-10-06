from app.tools.performance_report_tool import PerformanceReportTool


tool = PerformanceReportTool()

result = tool.generate_report(
    "data/execution_logs.csv"
)

print(result)