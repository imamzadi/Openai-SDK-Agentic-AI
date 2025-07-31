# Stream / Global level
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_default_openai_client, set_tracing_disabled
import os
from dotenv import load_dotenv
import asyncio
from openai.types.responses import ResponseTextDeltaEvent

# Load .env
load_dotenv()

# Disable tracing globally
set_tracing_disabled(True)

# Global client
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Global model
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)

# Set client as default globally
set_default_openai_client(client)

# Global agent
agent = Agent(
    name="Test",
    instructions="Provide simple answer",
    model=model
)

# Stream / Global level
async def run_stream_global():
    print("\n--- Streaming Global ---")
    print("Streaming Output: ", end="", flush=True)
    result = Runner.run_streamed(agent, "Tell me a joke.")
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

#  Run stream
if __name__ == "__main__":
    asyncio.run(run_stream_global())
