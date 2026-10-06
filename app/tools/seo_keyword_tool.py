import pandas as pd


class SEOKeywordTool:

    def classify_keyword(self, keyword):
        keyword_lower = keyword.lower()

        if any(word in keyword_lower for word in ["buy", "price", "purchase"]):
            return "Transactional"

        if any(word in keyword_lower for word in ["tutorial", "how", "guide", "course"]):
            return "Informational"

        if any(word in keyword_lower for word in ["best", "services", "developer", "framework"]):
            return "Commercial"

        return "Informational"

    def classify_keywords(self, file_path):
        data = pd.read_csv(file_path)

        results = []

        for _, row in data.iterrows():
            keyword = row["keyword"]

            category = self.classify_keyword(keyword)

            action = self.map_to_action(category)

            results.append({
                "keyword": keyword,
                "classification": category,
                "recommended_action": action
            })

        return results

    def map_to_action(self, classification):
        mapping = {
            "Informational": "Create educational content or blog",
            "Commercial": "Create comparison or service-focused content",
            "Transactional": "Optimize product/service landing page"
        }

        return mapping.get(
            classification,
            "Review keyword manually"
        )