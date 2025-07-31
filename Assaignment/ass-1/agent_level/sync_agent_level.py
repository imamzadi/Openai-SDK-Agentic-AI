# Sync / Agent level
from openai import AsyncOpenAI
from agents import Agent,Runner,OpenAIChatCompletionsModel
import os
from dotenv import load_dotenv


load_dotenv()

client = AsyncOpenAI(
      api_key=os.getenv("GEMINI_API_KEY"),
      base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
      )


model = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client)


agent = Agent(
      name= "Test",
      instructions= "Provide simple answer",
      model=model
)


# --- 2. sync Run ---
def run_async_example():
    res = Runner.run_sync(agent, "What is the purpose of AI?")
    print("Async Response:", res.final_output)

    
run_async_example()