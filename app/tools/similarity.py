from difflib import SequenceMatcher


class SimilarityTool:

    def calculate_similarity(self, text1, text2):
        return SequenceMatcher(
            None,
            text1.lower(),
            text2.lower()
        ).ratio()