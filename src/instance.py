from openai import OpenAI
from config import Config

config = Config()

openai_client = OpenAI(api_key=config.openai_key)