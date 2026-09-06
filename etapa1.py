#Vamos começar descobrindo quanto vale uma moeda em relação a outra! Crie um arquivo chamado etapa1.py. Importe o módulo requests. Crie uma função chamada buscar_cotacao(moeda_base, moeda_destino). Ela deve acessar a AwesomeAPI (https://economia.awesomeapi.com.br/json/last/ ) e devolver o valor atual da cotação. Exiba o valor no terminal com print(). Dica: o formato da URL é assim: https://economia.awesomeapi.com.br/json/last/USD-BRL

#Agora que já conseguimos buscar a cotação, vamos converter valores! Crie uma nova função chamada converter(valor, cotacao). Ela deve multiplicar o valor pela cotação e devolver o resultado. Peça ao usuário um valor e exiba o resultado da conversão.

#Vamos guardar as conversões feitas! Crie uma função registrar_historico(moeda, valor, resultado). Ela deve adicionar essas informações a uma lista chamada historico. Ao final, mostre todas as conversões já feitas.


import requests

def buscarCotacao(moedaBase, moedaDestino):
    urlBase = 'https://economia.awesomeapi.com.br/json/last/'
    url = urlBase + moedaBase + "-" + moedaDestino
    resposta = requests.get(url)

    dadosJson = resposta.json()

    chaveMoeda = moedaBase+moedaDestino
    cotacao = float(dadosJson[chaveMoeda]['bid'])

    return cotacao
    

def converter(valor, cotacao):

    valorConvertido = cotacao * valor

    return valorConvertido


listaRegistros = []
def registrarHistorico(moeda, valor, resultado):
    conversao = {
        'moeda': moeda,
        'valor': valor,
        'resultado': resultado
    }

    listaRegistros.append(conversao)

moedaBase = input('Digite a moeda de origem:').upper()
moedaDestino = input('Digite a moeda destino: ').upper()
valor = float(input('Digite o valor que deseja converter:'))

cotacao = buscarCotacao(moedaBase, moedaDestino)
print(f'A cotação atual é: {cotacao:.2f}')

valorFinal = converter(valor, cotacao)
print(f'O valor convertido é: {valorFinal:.2f}')

registrarHistorico(
    moedaBase + ' para ' + moedaDestino, 
    valor,
    valorFinal
)

print('Histórico de conversão:')
for conversao in listaRegistros:
    print(f'{conversao['moeda']} | Valor: {conversao['valor']:.2f} | Resultado: {conversao['resultado']:.2f}')
    