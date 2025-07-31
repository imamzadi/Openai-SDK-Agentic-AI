# run / Global level
from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# No need to use set_default_openai_client or set_tracing_disabled for run-level
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)

agent = Agent(
    name="Test",
    instructions="Provide simple answer",
    model=model
)

def main():
    run_config = RunConfig(model=model)  # optional: include tools, tracing, etc.
    res = Runner.run_sync(agent, "what is life",run_config=RunConfig)
    print(res.final_output)

main()
