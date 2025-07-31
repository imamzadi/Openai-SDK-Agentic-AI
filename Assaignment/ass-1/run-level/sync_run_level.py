# Sync / Run level

from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# --- Gemini Client ---
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# --- Model ---
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

# --- Agent ---
agent = Agent(
    name="RunLevelAgent",
    instructions="Answer simply and helpfully."
)

# --- RunConfig ---
run_config = RunConfig(
    model=model
)

# --- 2. Sync Run ---
def run_sync_example():
    print("\n--- Run Sync ---")
    result = Runner.run_sync(agent, "Define happiness.", run_config=run_config)
    print("Sync Run Result:", result.final_output)

# --- Main Method ---
run_sync_example()
