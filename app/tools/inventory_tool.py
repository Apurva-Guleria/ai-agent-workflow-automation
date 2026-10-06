import pandas as pd
from app.tools.calculator import Calculator


class InventoryTool:

    def __init__(self):
        self.calculator = Calculator()

    def find_restock_items(self, file_path):
        data = pd.read_csv(file_path)

        restock_items = data[
            data["current_stock"] < data["minimum_stock"]
        ].copy()

        restock_items["reorder_quantity"] = restock_items.apply(
            lambda row: self.calculator.subtract(
                row["minimum_stock"],
                row["current_stock"]
            ),
            axis=1
        )

        return restock_items