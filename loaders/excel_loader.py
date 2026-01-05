import pandas as pd
from loaders.base_loader import DocumentReader

class ExcelLoader(DocumentReader):
  def __init__(self, path: str):
    self.path = path
    
    
  def load(self) -> str:
    df = pd.read_excel(self.path, header = None)
    df = df.fillna('')
    
    return df.astype(str).fillna('').to_string(index = False, header = False)
  