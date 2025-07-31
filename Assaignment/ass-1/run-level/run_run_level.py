# Run / Run level
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables from .env file
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

# --- Run Level (Async run) ---
async def main():
    result = await Runner.run(agent, "What is the speed of light?", run_config=run_config)
    print(result.final_output)

# Execute
asyncio.run(main())
