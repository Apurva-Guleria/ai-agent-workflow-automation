from app.tools.duplicate_product_tool import DuplicateProductTool


tool = DuplicateProductTool()

result = tool.find_duplicates(
    "data/duplicate_products.csv"
)

for item in result:
    print(item)