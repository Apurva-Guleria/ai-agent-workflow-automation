from pathlib import Path

from app.tools.csv_tool import CSVTool
from app.tools.calculator import Calculator
from app.tools.inventory_tool import InventoryTool
from app.tools.price_validation_tool import PriceValidationTool
from app.tools.vendor_file_tool import VendorFileTool
from app.tools.product_description_tool import ProductDescriptionTool
from app.tools.duplicate_product_tool import DuplicateProductTool
from app.tools.marketing_campaign_tool import MarketingCampaignTool
from app.tools.seo_keyword_tool import SEOKeywordTool
from app.tools.employee_task_tool import EmployeeTaskTool
from app.tools.performance_report_tool import PerformanceReportTool
from app.tools.order_status_tool import OrderStatusTool


class ToolRegistry:

    def __init__(self):

        # Project root directory
        self.base_dir = Path(__file__).resolve().parent.parent.parent

        # Data directory
        self.data_dir = self.base_dir / "data"

        # Reusable tools
        self.tools = {
            "csv_reader": CSVTool(),
            "calculator": Calculator(),
            "inventory": InventoryTool(),
            "price_validation": PriceValidationTool(),
            "vendor_file": VendorFileTool(),
            "product_description": ProductDescriptionTool(),
            "duplicate_product": DuplicateProductTool(),
            "marketing_campaign": MarketingCampaignTool(),
            "seo_keyword": SEOKeywordTool(),
            "employee_task": EmployeeTaskTool(),
            "performance_report": PerformanceReportTool(),
            "order_status": OrderStatusTool(),
        }

        # Workflow execution handlers
        self.workflow_handlers = {
            "WF001": self.execute_inventory_restock,
            "WF002": self.execute_price_validation,
            "WF003": self.execute_vendor_file_processing,
            "WF004": self.execute_product_description,
            "WF005": self.execute_order_status,
            "WF006": self.execute_duplicate_detection,
            "WF007": self.execute_marketing_campaign,
            "WF008": self.execute_seo_keyword_classification,
            "WF009": self.execute_employee_task_assignment,
            "WF010": self.execute_performance_report,
        }

    def get_tool(self, tool_name):

        tool = self.tools.get(tool_name)

        if not tool:
            raise ValueError(f"Tool '{tool_name}' not found")

        return tool

    def get_tools_for_workflow(self, tools_required):
        tools_text = str(tools_required).lower()

        selected_tools = []

        if "csv" in tools_text or "csv/database reader" in tools_text:
            selected_tools.append("csv_reader")

        if "excel" in tools_text:
            selected_tools.append("vendor_file")

        if "calculator" in tools_text:
            selected_tools.append("calculator")

        if "inventory" in tools_text:
            selected_tools.append("inventory")

        if "vendor" in tools_text or "data validation" in tools_text:
            selected_tools.append("vendor_file")

        if "text validation" in tools_text:
            selected_tools.append("product_description")

        if "similarity" in tools_text:
            selected_tools.append("duplicate_product")

        if "llm" in tools_text and "product data" in tools_text:
            selected_tools.append("marketing_campaign")

        if "llm/classifier" in tools_text or "classification" in tools_text:
            selected_tools.append("seo_keyword")

        if "ranking" in tools_text or "assignment" in tools_text:
            selected_tools.append("employee_task")

        if "order database/api" in tools_text or "order" in tools_text:
            selected_tools.append("order_status")

        if "reporting" in tools_text or "performance" in tools_text or "metrics" in tools_text:
            selected_tools.append("performance_report")

        # Remove duplicates while preserving order
        return list(dict.fromkeys(selected_tools))

    def execute_workflow(self, workflow_id, user_request=None):

        # WF005 needs the user's order ID
        if workflow_id == "WF005":
            return self.execute_order_status(user_request)

        handler = self.workflow_handlers.get(workflow_id)

        if not handler:
            raise ValueError(
                f"No execution handler registered for {workflow_id}"
            )

        return handler()

    # ---------------------------------------------------------
    # WF001 - Inventory Restock Check
    # ---------------------------------------------------------

    def execute_inventory_restock(self):

        inventory_tool = self.get_tool("inventory")

        file_path = self.data_dir / "inventory.csv"

        result = inventory_tool.find_restock_items(
            str(file_path)
        )

        return result.to_dict(orient="records")

    # ---------------------------------------------------------
    # WF002 - Product Price Validation
    # ---------------------------------------------------------

    def execute_price_validation(self):

        price_tool = self.get_tool("price_validation")

        file_path = self.data_dir / "products.csv"

        result = price_tool.find_price_differences(
            str(file_path),
            threshold=10
        )

        return result.to_dict(orient="records")

    # ---------------------------------------------------------
    # WF003 - Vendor File Processing
    # ---------------------------------------------------------

    def execute_vendor_file_processing(self):

        vendor_tool = self.get_tool("vendor_file")

        file_path = self.data_dir / "vendor_data.csv"

        result = vendor_tool.process_file(
            str(file_path)
        )

        return result

    # ---------------------------------------------------------
    # WF004 - Product Description Generator
    # ---------------------------------------------------------

    def execute_product_description(self):

        product_tool = self.get_tool("product_description")

        file_path = self.data_dir / "product_description_input.csv"

        result = product_tool.generate_description(
            str(file_path)
        )

        return result

    # ---------------------------------------------------------
    # WF005 - Customer Order Status
    # ---------------------------------------------------------

    def execute_order_status(self, user_request):

        import re

        if not user_request:
            return {
                "status": "error",
                "message": "Please provide an order ID."
            }

        match = re.search(
            r"\bORD-?\d+\b",
            user_request.upper()
        )

        if not match:
            return {
                "status": "error",
                "message": "Please provide a valid order ID."
            }

        order_id = match.group()

        order_tool = self.get_tool("order_status")

        file_path = self.data_dir / "orders.csv"

        return order_tool.get_order_status(
            str(file_path),
            order_id
        )

    # ---------------------------------------------------------
    # WF006 - Duplicate Product Detection
    # ---------------------------------------------------------

    def execute_duplicate_detection(self):

        duplicate_tool = self.get_tool("duplicate_product")

        file_path = self.data_dir / "duplicate_products.csv"

        result = duplicate_tool.find_duplicates(
            str(file_path)
        )

        return result

    # ---------------------------------------------------------
    # WF007 - Marketing Campaign Brief
    # ---------------------------------------------------------

    def execute_marketing_campaign(self):

        marketing_tool = self.get_tool("marketing_campaign")

        file_path = self.data_dir / "marketing_campaign_input.csv"

        result = marketing_tool.generate_campaign_brief(
            str(file_path)
        )

        return result

    # ---------------------------------------------------------
    # WF008 - SEO Keyword Classification
    # ---------------------------------------------------------

    def execute_seo_keyword_classification(self):

        seo_tool = self.get_tool("seo_keyword")

        file_path = self.data_dir / "seo_keywords.csv"

        result = seo_tool.classify_keywords(
            str(file_path)
        )

        return result

    # ---------------------------------------------------------
    # WF009 - Employee Task Assignment
    # ---------------------------------------------------------

    def execute_employee_task_assignment(self):

        employee_tool = self.get_tool("employee_task")

        tasks_file = self.data_dir / "employee_tasks.csv"
        employees_file = self.data_dir / "employees.csv"

        result = employee_tool.assign_tasks(
            str(tasks_file),
            str(employees_file)
        )

        return result

    # ---------------------------------------------------------
    # WF010 - Workflow Performance Report
    # ---------------------------------------------------------

    def execute_performance_report(self):

        performance_tool = self.get_tool("performance_report")

        file_path = self.data_dir / "execution_logs.csv"

        result = performance_tool.generate_report(
            str(file_path)
        )

        return result