from app.tools.vendor_file_tool import VendorFileTool


tool = VendorFileTool()

result = tool.process_file(
    "data/vendor_data.csv"
)

print(result)