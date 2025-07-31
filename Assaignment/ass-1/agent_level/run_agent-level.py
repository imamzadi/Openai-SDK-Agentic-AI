# Run / Agent level 
from openai import AsyncOpenAI
from agents import Agent,Runner,OpenAIChatCompletionsModel
import asyncio
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

# --- 1.Run ---
async def run_example():
    res = await Runner.run(agent, "What is life?")
    print("Sync Response:", res.final_output)
asyncio.run(run_example())





# run - agar hum chahty hain ky hamry paas jo agents hain hum chahty hain ko wo bhi run ho aur sath hee doosra kaam bhi ho to run use karty hain. Is chalany ky liye humen method ko `async` karna hoga.

# run_sync agar hum chahty hain ky hamary paas jo agents hain wo completedly execute hon aur phir doosra code agay chale then hum `run_sync` use karengy isy chalany ky liye `async` method nahi lagaingy. is mai ander async method hota hai.

# run_stream agar hum live response chahty hain llm se to hum run_stream use karty hain. is mai hamary paas streaming hoti hai word by words. Is mai ahamry paas buhat saari details
