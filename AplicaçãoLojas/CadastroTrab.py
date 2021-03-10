#!/usr/bin/env python3
from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['Carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
dados['Idade'] = datetime.now().year - nasc
if dados ['Carteira'] != 0:
    dados ['Contratação'] = int(input('Ano de contratação: '))
    dados ['Salário'] = float(input('Sálario:R$  '))
    dados ['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35)- datetime.now().year)
print('=-'*30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v} ')    
