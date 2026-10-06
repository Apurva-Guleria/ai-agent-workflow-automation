import pandas as pd
from app.tools.llm_tool import LLMTool


class ProductDescriptionTool:

    def __init__(self):
        self.llm = LLMTool()

    def generate_description(self, file_path):

        data = pd.read_csv(file_path)

        results = []

        for _, row in data.iterrows():

            product_name = row["product_name"]
            category = row["category"]
            features = row["features"]
            target_audience = row["target_audience"]

            if pd.isna(target_audience) or not str(target_audience).strip():
                target_audience = "general customers"

            prompt = f"""
Generate a short professional product description.

Product Name: {product_name}
Category: {category}
Features: {features}
Target Audience: {target_audience}

Requirements:
- 2 to 3 sentences
- Clear and professional
- Mention important features
- Do not invent specifications
"""

            description = self.llm.ask(prompt)

            results.append({
                "product_id": row["product_id"],
                "product_name": product_name,
                "description": description
            })

        return results