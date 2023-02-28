import requests
import json

nome = input(str('Qual o nome você quer consultar: '))
request = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}')
request = request.json()
periodos = (request[0]['res'])
data = (periodos[1]['periodo'])
inicio = data[1:5]
fim = data[6:10]
quantidade = (periodos[1]['frequencia'])
print(f'No período de {inicio} até {fim} o nome {nome} tem {quantidade} registros!')