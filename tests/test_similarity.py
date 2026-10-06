from app.tools.similarity import SimilarityTool

tool = SimilarityTool()

score = tool.calculate_similarity(
    "Wireless Mouse",
    "Wireless Mousse"
)

print("Similarity score:", score)