from loaders.base_loader import DocumentReader

class TXTLoader(DocumentReader):
  def __init__(self, text: str):
    self.text = text
    
    
  def load(self) -> str:
    return self.text
  