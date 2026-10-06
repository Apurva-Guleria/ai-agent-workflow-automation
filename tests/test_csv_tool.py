from app.tools.csv_tool import CSVTool


csv_tool = CSVTool()

data = csv_tool.read_csv("data/inventory.csv")

print(data)