from app.tools.inventory_tool import InventoryTool


inventory_tool = InventoryTool()

result = inventory_tool.find_restock_items(
    "data/inventory.csv"
)

print("\nProducts that need restocking:\n")
print(result)