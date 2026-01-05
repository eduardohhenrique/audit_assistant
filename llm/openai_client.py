from openai import OpenAI
from config.settings import OPENAI_API_KEY, MODEL_NAME
from llm.base_llm import BaseLLM

class OpenAIClient(BaseLLM):
  def __init__(self):
    self.client = OpenAI(api_key = OPENAI_API_KEY)
    
    
  def risk_analyze(self, text: str) -> str:
    prompt = f'''
 You are an auditing assistant.
Analyze the text and identify risks, inconsistencies, and possible points of attention.

Text:
{text}
'''

    response = self.client.chat.completions.create(
      model = MODEL_NAME,
      messages = [{'role': 'user', 'content': prompt}],
      temperature = 0.2
    )
    
    return response.choices[0]