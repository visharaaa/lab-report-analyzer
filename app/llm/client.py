"""
Client utilities for generating laboratory report explanations.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI


DEFAULT_MODEL = "gpt-5.6-luna"

load_dotenv()


def create_client() -> OpenAI:
    """
    Create an OpenAI client using the configured API key.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable is not set."
        )

    return OpenAI(api_key=api_key)


def generate_explanation(
    system_prompt: str,
    user_prompt: str,
    model: str | None = None,
) -> str:
    """
    Generate a laboratory report explanation using an LLM.

    This function makes a real API request when called.
    """

    client = create_client()

    response = client.responses.create(
        model=model or os.getenv("OPENAI_MODEL", DEFAULT_MODEL),
        instructions=system_prompt,
        input=user_prompt,
    )

    return response.output_text