import os

from dotenv import load_dotenv

load_dotenv()


def test_openai_api_key_is_configured():
    api_key = os.getenv("OPENAI_API_KEY")

    assert api_key is not None
    assert api_key.strip() != ""