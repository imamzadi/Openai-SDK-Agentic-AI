# Stream / Run level
from openai import AsyncOpenAI
from agents import Agent,Runner,OpenAIChatCompletionsModel,RunConfig
import os
from dotenv import load_dotenv
import asyncio
from openai.types.responses import ResponseTextDeltaEvent


load_dotenv()

client = AsyncOpenAI(
      api_key=os.getenv("GEMINI_API_KEY"),
      base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
      )


model = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client)


agent = Agent(
      name= "Test",
      instructions= "Provide simple answer"
)

run_config = RunConfig(
      model=model
)

# --- 3. Streaming Run ---
async def run_stream_example():
    print("\n--- Run Stream ---")
    print("Streaming Output: ", end="", flush=True)
    result = Runner.run_streamed(agent, "Tell me a joke.")
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

asyncio.run(run_stream_example)

