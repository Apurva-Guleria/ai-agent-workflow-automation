from app.tools.llm_tool import LLMTool


llm = LLMTool()

response = llm.ask(
    "In one short sentence, explain what an AI agent is."
)

print(response)