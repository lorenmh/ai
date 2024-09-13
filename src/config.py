import os
from pydantic_settings import BaseSettings

output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'output'))

class Config(BaseSettings):
    openai_key: str