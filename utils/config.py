import os
from dotenv import load_dotenv
from agno.models.openai import OpenAIChat
from datetime import datetime  # Importing datetime

load_dotenv()

def get_model(model_id="openai/gpt-4o-mini"):
    """
    Returns an Agno Model configured for OpenRouter.
    Default model is gpt-4o-mini via OpenRouter.
    """
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables.")
    
    return OpenAIChat(
        id=model_id,
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1"
    )
