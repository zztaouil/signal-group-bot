from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.models.openai import OpenAIChat
from agno.tools.wikipedia import WikipediaTools
from agno.tools.newspaper import NewspaperTools
import random
import requests

def get_agent(description, instructions, expected_output):
    agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[NewspaperTools()],
        description=description,
        instructions=instructions,
        expected_output=expected_output,
        # debug_mode=True,
        # show_tool_calls=False,
        # warnings=False,
        read_chat_history=True,
        add_history_to_messages=True,
        num_history_responses=10,
    )
    return agent


def generate_response(message):
    # agent = get_agent(
    #     description="You're an angry moroccan adult male.",
    #     instructions="Always respond in Moroccan dialect, no arabic letters, no translation. Don't offer assistance, just respond to the message Don't ask questions in your reponse. Use vulgar darija language when appropriate. Don't use emojis.",
    #     expected_output="A concise text message to the message sender that doesn't repeat previous responses",
    # )
    agent = get_agent(
        description="You're an angry recentful Moroccan male.",
        instructions="Don't help, just respond angrily to the message. Don't use emojis. Use insults.",
        expected_output="",
    )
    response = agent.run(f"{message}")
    return response.content
    # possibilities = [
    #     "kayna awda hadak",
    #     "n3al chitan",
    #     "fchkel hadchi",
    #     "blan",
    #     "ghyrha asahbi",
    #     "ok",
    #     "wlahila kayn",
    #     "hdra m39ola",
    # ]
    # return random.choice(possibilities)

def download_shrek():
    response = requests.get("https://shreks.corneroftheinter.net/?img=png")
    with open("shrek.png", "wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    agent = get_agent(
        description="You are a helpful assistant that can answer questions and help with tasks.",
        instructions="You are a helpful assistant that can answer questions and help with tasks.",
        expected_output="You are a helpful assistant that can answer questions and help with tasks.",
    )
    print(agent.print_response("What is the capital of France?"))