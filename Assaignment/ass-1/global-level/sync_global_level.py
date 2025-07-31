# Sync / Global level
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_default_openai_client, set_tracing_disabled
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Disable tracing globally (optional)
set_tracing_disabled(True)

# Global Client
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Global Model
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)

# Set client globally
set_default_openai_client(client)

# Global Agent
agent = Agent(
    name="Test",
    instructions="Provide simple answer",
    model=model
)

#  SYNC RUN using Global Level
def main():
    print("\n--- Sync Run (Global Level) ---")
    result = Runner.run_sync(agent, "What is the meaning of life?")
    print("Answer:", result.final_output)

# Execute
if __name__ == "__main__":
    main()
