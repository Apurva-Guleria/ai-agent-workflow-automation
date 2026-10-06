from app.tools.seo_keyword_tool import SEOKeywordTool


tool = SEOKeywordTool()

result = tool.classify_keywords(
    "data/seo_keywords.csv"
)

for item in result:
    print(item)