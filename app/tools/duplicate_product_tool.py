import pandas as pd
from app.tools.similarity import SimilarityTool


class DuplicateProductTool:

    def __init__(self):
        self.similarity_tool = SimilarityTool()

    def find_duplicates(self, file_path, threshold=0.80):
        data = pd.read_csv(file_path)

        duplicates = []

        for i in range(len(data)):
            for j in range(i + 1, len(data)):

                product_1 = data.iloc[i]
                product_2 = data.iloc[j]

                score = self.similarity_tool.calculate_similarity(
                    product_1["product_name"],
                    product_2["product_name"]
                )

                if score >= threshold:

                    if score >= 0.90:
                        confidence = "High"
                    elif score >= 0.80:
                        confidence = "Medium"
                    else:
                        confidence = "Low"

                    duplicates.append({
                        "product_1": product_1["product_name"],
                        "product_2": product_2["product_name"],
                        "similarity_score": round(score, 3),
                        "confidence": confidence
                    })

        return duplicates