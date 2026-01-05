import os

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MODEL_NAME = 'gpt-4o-mini'
USE_MOCK_LLM = True # Desative while using OpenAI API