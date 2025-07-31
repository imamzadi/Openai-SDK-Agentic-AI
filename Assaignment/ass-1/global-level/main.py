# Global level
from openai import AsyncOpenAI
from agents import Agent,Runner,OpenAIChatCompletionsModel,set_default_openai_client, set_tracing_disabled
import os
from dotenv import load_dotenv

load_dotenv()
set_tracing_disabled(True)
client = AsyncOpenAI(
      api_key=os.getenv("GEMINI_API_KEY"),
      base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
      )



model = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client)

set_default_openai_client(client)

agent = Agent(
      name= "Test",
      instructions= "Provide simple answer",
      model=model
)
 
def main():
      res = Runner.run_sync(agent,"what is life")
      print(res.final_output)
main()









# global_level/main.py
# import asyncio
# from agents import Runner
# from config import agent

# --- Sync Run ---
def run_sync_global():
    print("\n--- Global Sync ---")
    result = Runner.run_sync(agent, "Define success.")
    print("Sync Result:", result.final_output)

# # --- Async Run ---
# async def run_async_global():
#     print("\n--- Global Async ---")
#     result = await Runner.run_async(agent, "Explain gravity.")
#     print("Async Result:", result.final_output)

# # --- Stream Run ---
# async def run_stream_global():
#     print("\n--- Global Stream ---")
#     print("Streaming Output: ", end="", flush=True)
#     async for event in Runner.run_stream(agent, "Give a motivational quote."):
#         print(event.delta, end="", flush=True)
#     print()

# # --- Run All ---
# def main():
#     run_sync_global()
#     asyncio.run(run_async_global())
#     asyncio.run(run_stream_global())

# if __name__ == "__main__":
#     main()


