import requests
import json

nome = input(str('Qual o nome você quer consultar: '))
request = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}')
request = request.json()
periodos = (request[0]['res'])
total = len(periodos)
for n in range(0,total):
    data = (periodos[n]['periodo'])
    inicio = data[1:5]
    fim = data[6:10]
    quantidade = (periodos[n]['frequencia'])
    if inicio == '930[':
        print(f'No ano de 1930 nome {nome} teve {quantidade} registros!')
    else:
        print(f'No período de {inicio} até {fim} o nome {nome} teve {quantidade} registros!')
    