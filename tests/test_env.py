from dotenv import load_dotenv
import os

load_dotenv(
    r"C:\Users\apurv\Downloads\ai-agent-workflow-automation\.env"
)

print("TEST:", os.getenv("TEST_VALUE"))
print("API FOUND:", os.getenv("OPENAI_API_KEY") is not None)