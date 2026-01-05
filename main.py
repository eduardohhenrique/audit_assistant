from loaders.pdf_loader import PDFLoader
from loaders.excel_loader import ExcelLoader
from loaders.txt_loader import TXTLoader
from pipeline.audit_pipeline import Pipeline


def main():
  # Test loaders
  loader = PDFLoader('data\pdf\sample_pdf_2.pdf')
  #loader = TXTLoader('Paste here!')
  #loader = ExcelLoader('data\excel\sample_excel_1.xlsx')

  pipeline = Pipeline(loader)
  result = pipeline.run()
  
  print('-=-=Analyse Results=-=-')
  print(result)

if __name__ == '__main__':
  main()