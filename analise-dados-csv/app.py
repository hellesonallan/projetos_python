import pandas as pd

while True:
  try:
    arquivo = input("Insira o caminho do arquivo: ")
  except:
tabela_arquivo = pd.read_csv(arquivo)
print(tabela_arquivo)