from app.tools.product_description_tool import ProductDescriptionTool


tool = ProductDescriptionTool()

result = tool.generate_description(
    "data/product_description_input.csv"
)

for item in result:

    print("\nProduct:", item["product_name"])
    print("Description:", item["description"])