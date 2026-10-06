import pandas as pd


class OrderStatusTool:

    def get_order_status(self, file_path, order_id):
        data = pd.read_csv(file_path)

        order = data[data["order_id"] == order_id]

        if order.empty:
            return {
                "status": "error",
                "message": f"Order {order_id} was not found."
            }

        row = order.iloc[0]

        return {
            "status": "success",
            "order_id": row["order_id"],
            "customer_name": row["customer_name"],
            "product_name": row["product_name"],
            "order_status": row["status"],
            "estimated_delivery": row["estimated_delivery"]
        }