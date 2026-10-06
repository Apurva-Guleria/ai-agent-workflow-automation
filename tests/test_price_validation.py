from app.tools.price_validation_tool import PriceValidationTool


tool = PriceValidationTool()

result = tool.find_price_differences(
    "data/products.csv",
    threshold=10
)

print(result.to_string(index=False))