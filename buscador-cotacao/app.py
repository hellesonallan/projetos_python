import requests
from tkinter import *

def pegar_contacao():
  requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")

  requisicao_dic = requisicao.json()

  cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
  cotacao_euro = requisicao_dic["EURBRL"]["bid"]
  cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

  texto = f'''
  Dólar: {cotacao_dolar}
  Euro: {cotacao_euro}
  Bitcoin: {cotacao_btc}
  '''

  texto_cotacoes["text"] = texto

janela = Tk()

janela.title("Cotação Atual das Moedas")

texto_orientacao = Label(janela, text="Clique no botão para exibir a cotação das moedas")
texto_orientacao.grid(column=0, row=0, padx=20, pady=10)

botao = Button(janela, text="Buscar Cotações", command=pegar_contacao)
botao.grid(column=0, row=1)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2)

janela.mainloop()