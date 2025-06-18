from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.models.openai import OpenAIChat


def get_agent(description, instructions, expected_output):
    agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        description=description,
        instructions=instructions,
        expected_output=expected_output,
        # debug_mode=True,
        # show_tool_calls=False,
        # warnings=False,
        read_chat_history=True,
        add_history_to_messages=True,
        
    )
    return agent


def generate_response(message):
    agent = get_agent(
        description="You're moroccan adult male.",
        instructions="Always respond in Moroccan dialect, no arabic letters, no translation. Don't offer assistance, just respond to the message. Review the conversation history to avoid repeating yourself. Provide fresh and unique responses each time while maintaining a consistent personality. Don't ask questions in your reponse.",
        expected_output="A concise text message to the message sender that doesn't repeat previous responses",
    )
    response = agent.run(f"respond to the following message: {message}")
    return response.content

if __name__ == "__main__":
    agent = get_agent(
        description="You are a helpful assistant that can answer questions and help with tasks.",
        instructions="You are a helpful assistant that can answer questions and help with tasks.",
        expected_output="You are a helpful assistant that can answer questions and help with tasks.",
    )
    print(agent.print_response("What is the capital of France?"))