import json
import requests

req = None

# Consumindo a API fazendo as requisições para obter as informações das moedas.
def requisicao(titulo):
    try:
        req = requests.get("https://economia.awesomeapi.com.br/last/" + titulo)
        iRETORNO = json.loads(req.text)
        return iRETORNO

    except Exception as e:
        print('Não foi possível fazer a requisição', e)
        return None

    
# Os dados, inicialmente, vêm em um dicionário, que está contido em outro.
# A função abaixo trata de separar os dicionários, e permitir o uso daquele que realmente importa ao programa.
def descompactar(conteudo, cont):
    descompactado = conteudo[cont]
    return descompactado


def printa_detalhe(descompactado):
    print('Nome:', descompactado['name'])
    print('Alta:', descompactado['high'])
    print('Baixa:', descompactado['low'])
    print('Variação hoje:', descompactado['varBid'])
    print('Porcentagem de Variação:', descompactado['pctChange'])
    print('Dia e hora da requisição:', descompactado['create_date'])
    print('Valor de Compra:', descompactado['bid'])
    print('Valor para Venda:', descompactado['ask'])

moeda = input('Digite uma moeda a ser consultada:\nOpções:\n\n"USD-BRL, EUR-BRL, BTC-BRL": ')
valor = requisicao(moeda)

if moeda == 'USD-BRL':
    cont = 'USDBRL'
    des = descompactar(valor, cont)
if moeda == 'EUR-BRL':
    cont = 'EURBRL'
    des = descompactar(valor, cont)
if moeda == 'BTC-BRL':
    cont = 'BTCBRL'
    des = descompactar(valor, cont)

printa_detalhe(des)
