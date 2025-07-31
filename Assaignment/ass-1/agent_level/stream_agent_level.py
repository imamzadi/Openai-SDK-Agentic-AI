# Stream / Agent Level
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel
import os
from dotenv import load_dotenv
import asyncio
from openai.types.responses import ResponseTextDeltaEvent

load_dotenv()

# Gemini Client
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

# Agent
agent = Agent(
    name="Test",
    instructions="Provide simple answer",
    model=model
)

# Streaming Function
async def run_stream_example():
    print("Streamed Response: ", end="", flush=True)
    result = Runner.run_streamed(agent, "Tell me a joke.")
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

# Run the Stream
asyncio.run(run_stream_example())
