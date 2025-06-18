from agno.agent import Agent
from agno.models.anthropic import Claude

def get_agent(description, instructions, expected_output):
    agent = Agent(
        model=Claude(id="claude-3-5-haiku-20241022"),
        description=description,
        instructions=instructions,
        expected_output=expected_output,
        add_references=False,
        search_knowledge=True,
        # debug_mode=True,
        # show_tool_calls=False,
        # warnings=False,
        read_chat_history=False,
    )
    return agent


def generate_response(message):
    agent = get_agent(
        description="You are a Moroccan person that engage in fun conversations with the user",
        instructions="Always respond in Moroccan dialect, no arabic letters, no translation.",
        expected_output="A concise text message to the message sender",
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