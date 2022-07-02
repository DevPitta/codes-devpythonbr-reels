"""
This code uses the PySimpleGUI and forex-python libraries
and makes a window to show the current currency.

-> Requirements:
    . pip install pysimplegui
    . pip install forex-python
"""

import PySimpleGUI as sg
from forex_python.converter import CurrencyRates

currency = CurrencyRates()

layout = [
    [sg.Text('Digite o valor em Dólar')],
    [sg.InputText(key='valor')],
    [sg.Button('Cotação'), sg.Button('Cancelar')],
    [sg.Text('', key='texto_cotacao')],
]

janela = sg.Window('Sistema de Cotações', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Cotação':
        valor = valores['valor']
        cotacao = round(currency.convert('USD', 'BRL', int(valor)), 2)
        janela['texto_cotacao'].update(f'A cotação do ${valor} é de R${cotacao}')

janela.close()
