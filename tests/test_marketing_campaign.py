from app.tools.marketing_campaign_tool import MarketingCampaignTool


tool = MarketingCampaignTool()

result = tool.generate_campaign_brief(
    "data/marketing_campaign_input.csv"
)

for item in result:
    print("\nCampaign:", item["campaign_name"])
    print("Product:", item["product_name"])
    print("Brief:")
    print(item["brief"])