import pandas as pd


class PerformanceReportTool:

    def generate_report(self, file_path):
        data = pd.read_csv(file_path)

        total_executions = len(data)

        success_count = len(
            data[data["status"] == "success"]
        )

        failure_count = len(
            data[data["status"] == "failure"]
        )

        failure_rate = (
            failure_count / total_executions * 100
            if total_executions > 0
            else 0
        )

        average_duration = (
            data["duration_seconds"].mean()
            if total_executions > 0
            else 0
        )

        failure_by_workflow = (
            data[data["status"] == "failure"]
            .groupby("workflow_id")
            .size()
            .sort_values(ascending=False)
        )

        most_failing_workflow = (
            failure_by_workflow.index[0]
            if not failure_by_workflow.empty
            else None
        )

        most_failure_count = (
            int(failure_by_workflow.iloc[0])
            if not failure_by_workflow.empty
            else 0
        )

        return {
            "total_executions": total_executions,
            "successful_executions": success_count,
            "failed_executions": failure_count,
            "failure_rate_percent": round(failure_rate, 2),
            "average_duration_seconds": round(float(data["duration_seconds"].mean()), 2),
            "most_failing_workflow": most_failing_workflow,
            "most_failure_count": most_failure_count
        }