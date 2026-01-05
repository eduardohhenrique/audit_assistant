from preprocess.text_preprocess import TextPreprocessor
from llm.openai_client import OpenAIClient
from llm.mock_llm import MockLLM
from config.settings import USE_MOCK_LLM

class Pipeline:
  def __init__(self, loader):
    self.loader = loader
    self.preprocessor = TextPreprocessor()
    
    if USE_MOCK_LLM:
      self.llm = MockLLM()
      
    else:
      self.llm = OpenAIClient()
    
    
  def run(self):
    raw_text = self.loader.load()
    clean_text = self.preprocessor.clean(raw_text)
    result = self.llm.risk_analyze(clean_text)
    
    return result