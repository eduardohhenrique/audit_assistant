from loaders.pdf_loader import PDFLoader
from loaders.excel_loader import ExcelLoader

def main():
  #loader = PDFLoader('data\pdf\sample_pdf_1.pdf')
  loader = ExcelLoader('data\excel\sample_excel_1.xlsx')

  text = loader.load()

  print('-=-=Texto Extraído=-=-')
  print(text[:1000])

if __name__ == '__main__':
  main()