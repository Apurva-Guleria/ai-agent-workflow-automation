from app.tools.csv_tool import CSVTool
from app.tools.calculator import Calculator
from app.tools.inventory_tool import InventoryTool
from app.tools.price_validation_tool import PriceValidationTool
from app.tools.vendor_file_tool import VendorFileTool
from app.tools.duplicate_product_tool import DuplicateProductTool
from app.tools.marketing_campaign_tool import MarketingCampaignTool
from app.tools.seo_keyword_tool import SEOKeywordTool
from app.tools.employee_task_tool import EmployeeTaskTool
from app.tools.performance_report_tool import PerformanceReportTool
from app.tools.order_status_tool import OrderStatusTool

class ToolRegistry:

    def __init__(self):
        self.tools = {
            "csv_reader": CSVTool(),
            "calculator": Calculator(),
            "inventory": InventoryTool(),
            "price_validation": PriceValidationTool(),
            "vendor_file": VendorFileTool(),
            "duplicate_product": DuplicateProductTool(),
            "marketing_campaign": MarketingCampaignTool(),
            "seo_keyword": SEOKeywordTool(),
            "employee_task": EmployeeTaskTool(),
            "performance_report": PerformanceReportTool(),
            "order_status": OrderStatusTool()
        }

        self.workflow_handlers = {
            "WF001": self.execute_inventory_restock,
            "WF002": self.execute_price_validation,
            "WF003": self.execute_vendor_file_processing,
            "WF005": self.execute_order_status,
            "WF006": self.execute_duplicate_detection,
            "WF007": self.execute_marketing_campaign,
            "WF008": self.execute_seo_keyword_classification,
            "WF009": self.execute_employee_task_assignment,
            "WF010": self.execute_performance_report


        }

    def get_tool(self, tool_name):

        tool = self.tools.get(tool_name)

        if not tool:
            raise ValueError(f"Tool '{tool_name}' not found")

        return tool

    def get_tools_for_workflow(self, tools_required):
        selected_tools = []
        tools_text = str(tools_required).lower()

        if (
                "reporting" in tools_text
                or "performance" in tools_text
                or "metrics" in tools_text
                or "log analysis" in tools_text
        ):
            selected_tools.append("performance_report")
            return selected_tools

        if "csv" in tools_text:
            selected_tools.append("csv_reader")

        if "calculator" in tools_text:
            selected_tools.append("calculator")

        if "inventory" in tools_text:
            selected_tools.append("inventory")

        if "vendor" in tools_text:
            selected_tools.append("vendor_file")

        if "similarity" in tools_text:
            selected_tools.append("duplicate_product")

        if "llm" in tools_text and "product data" in tools_text:
            selected_tools.append("marketing_campaign")

        if "classification" in tools_text or "mapping" in tools_text:
            selected_tools.append("seo_keyword")

        if "ranking" in tools_text or "assignment" in tools_text:
            selected_tools.append("employee_task")

        if "database" in tools_text or "api" in tools_text or "order" in tools_text:
            selected_tools.append("order_status")

        return selected_tools

    def execute_workflow(self, workflow_id, user_request=None):

        if workflow_id == "WF005":
            return self.execute_order_status(user_request)

        handler = self.workflow_handlers.get(workflow_id)

        if not handler:
            raise ValueError(
                f"No execution handler registered for {workflow_id}"
            )

        return handler()

    def execute_inventory_restock(self):

        inventory_tool = self.get_tool("inventory")

        result = inventory_tool.find_restock_items(
            "data/inventory.csv"
        )

        return result.to_dict(orient="records")

    def execute_price_validation(self):

        price_tool = self.get_tool("price_validation")

        result = price_tool.find_price_differences(
            "data/products.csv",
            threshold=10
        )

        return result.to_dict(orient="records")

    def execute_vendor_file_processing(self):

        vendor_tool = self.get_tool("vendor_file")

        result = vendor_tool.process_file(
            "data/vendor_data.csv"
        )

        return result

    def execute_duplicate_detection(self):
        duplicate_tool = self.get_tool("duplicate_product")

        result = duplicate_tool.find_duplicates(
            "data/duplicate_products.csv"
        )

        return result

    def execute_marketing_campaign(self):
        marketing_tool = self.get_tool("marketing_campaign")

        result = marketing_tool.generate_campaign_brief(
            "data/marketing_campaign_input.csv"
        )

        return result

    def execute_seo_keyword_classification(self):
        seo_tool = self.get_tool("seo_keyword")

        result = seo_tool.classify_keywords(
            "data/seo_keywords.csv"
        )

        return result

    def execute_employee_task_assignment(self):
        employee_tool = self.get_tool("employee_task")

        result = employee_tool.assign_tasks(
            "data/employee_tasks.csv",
            "data/employees.csv"
        )

        return result

    def execute_performance_report(self):
        performance_tool = self.get_tool("performance_report")

        result = performance_tool.generate_report(
            "data/execution_logs.csv"
        )

        return result

    def execute_order_status(self, user_request):
        import re

        match = re.search(
            r"\bORD\d+\b",
            user_request.upper()
        )

        if not match:
            return {
                "status": "error",
                "message": "Please provide a valid order ID."
            }

        order_id = match.group()

        order_tool = self.get_tool("order_status")

        return order_tool.get_order_status(
            "data/orders.csv",
            order_id
        )