import pdfplumber
from loaders.base_loader import DocumentReader

class PDFLoader(DocumentReader):
  def __init__(self, path: str):
    self.path = path
    
  
  def load(self) -> str:
    text = ''
    
    with pdfplumber.open(self.path) as pdf:
      for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
          text += page_text + '\n'
          
    return text
  