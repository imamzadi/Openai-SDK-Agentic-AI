# Run level
from openai import AsyncOpenAI
from agents import Agent,Runner,OpenAIChatCompletionsModel,RunConfig
import os
from dotenv import load_dotenv
import asyncio

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


async def main():
      res = await Runner.run(agent,"what is life", run_config=run_config)
      print(res.final_output)
      
asyncio.run(main())











