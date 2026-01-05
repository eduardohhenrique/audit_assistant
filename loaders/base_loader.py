from abc import ABC, abstractmethod

class DocumentReader(ABC):
  @abstractmethod
  def load(self) -> str:
    pass
  
  