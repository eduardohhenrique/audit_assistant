from loaders.pdf_loader import PDFLoader
from loaders.excel_loader import ExcelLoader
from loaders.txt_loader import TXTLoader
from preprocess.text_preprocess import TextPreprocessor


def main():
  # Teste de loaders
  loader = PDFLoader('data\pdf\sample_pdf_1.pdf')
  #loader = TXTLoader('Cole aqui!')
  #loader = ExcelLoader('data\excel\sample_excel_1.xlsx')

  text = loader.load()

  print('-=-=Texto Extraído=-=-')
  print(text[:1000])
  
  preprocessor = TextPreprocessor()
  text = preprocessor.clean(text)
  
  print('-=-=Texto Preprocessado=-=-')
  print(text[:1000])

if __name__ == '__main__':
  main()