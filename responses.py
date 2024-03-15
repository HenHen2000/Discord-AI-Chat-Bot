from random import choice, randint
import openai


def get_response(user_input: str) -> str:
    lowerd: str = user_input.lower()
    return openai.Completion.create(
    engine="gpt-3.5-turbo-0125",
    prompt=f"{lowerd}",
    max_tokens=2048,
    temperature=0.5,
    )