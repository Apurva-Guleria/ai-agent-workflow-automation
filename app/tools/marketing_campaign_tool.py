import pandas as pd
from app.tools.llm_tool import LLMTool


class MarketingCampaignTool:

    def __init__(self):
        self.llm = LLMTool()

    def generate_campaign_brief(self, file_path):
        data = pd.read_csv(file_path)

        results = []

        for _, row in data.iterrows():

            prompt = f"""
Create a concise marketing campaign brief.

Campaign Name: {row["campaign_name"]}
Product: {row["product_name"]}
Target Audience: {row["target_audience"]}
Goal: {row["goal"]}
Key Message: {row["key_message"]}

Return the response with exactly these sections:

Campaign Objective:
Target Audience:
Key Message:
Marketing Ideas:
Call To Action:

Keep it practical and concise.
Do not invent product specifications.

Use ONLY facts explicitly provided in the input.

Do not invent:
- discounts or percentages
- prices or offers
- mobile apps or voice control
- technical specifications
- product features not provided
- partnerships or promotions
- specific marketing channels unless provided

If a detail is not provided, keep the recommendation generic.

The Call To Action must not introduce a discount, offer, or product feature that was not provided.
"""

            brief = self.llm.ask(prompt)

            results.append({
                "campaign_name": row["campaign_name"],
                "product_name": row["product_name"],
                "brief": brief
            })

        return results