from loaders.pdf_loader import PDFLoader

def main():
  loader = PDFLoader('data\pdf\sample_pdf_1.pdf')
  text = loader.load()

  print('-=-=Texto Extraído=-=-')
  print(text[:1000])

if __name__ == '__main__':
  main()