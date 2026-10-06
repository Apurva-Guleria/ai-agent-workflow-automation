from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


class LLMTool:

    def __init__(self):
        self.llm = ChatGroq(
            model="openai/gpt-oss-120b",
            temperature=0
        )

    def ask(self, prompt):
        response = self.llm.invoke(prompt)
        return response.content