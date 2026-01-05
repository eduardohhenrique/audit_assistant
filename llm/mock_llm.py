from llm.base_llm import BaseLLM

'''
  Used portuguese words because of the files that I have as sample.
'''
class MockLLM(BaseLLM):
  def risk_analyze(self, text: str) -> str:
    if "despesa" in text or "custo" in text:
      return "Possível risco: aumento de despesas sem justificativa clara."
    
    if "receita" in text:
      return "Atenção: validar consistência dos dados de receita."
    return "Nenhum risco relevante identificado."
