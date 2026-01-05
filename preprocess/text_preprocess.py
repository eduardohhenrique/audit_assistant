import re
from unidecode import unidecode

class TextPreprocessor:
  def clean(self, text: str) -> str:
    text = text.lower()
    text = unidecode(text) # Remover acentos
    text = re.sub(r'\s+', ' ', text) # Remover espaços
    
    return text.strip()