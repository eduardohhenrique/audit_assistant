from abc import ABC, abstractmethod

class BaseLLM:
  @abstractmethod
  def risk_analyze(self, text: str):
    pass