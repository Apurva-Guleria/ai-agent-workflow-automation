from app.tools.order_status_tool import OrderStatusTool


tool = OrderStatusTool()

result = tool.get_order_status(
    "data/orders.csv",
    "ORD999"
)

print(result)