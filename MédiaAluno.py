#!/usr/bin/env python3
sistema = dict()
sistema ['aluno'] = str(input('Nome: '))
sistema['média'] = float(input(f'Média de {sistema["aluno"]}: '))
if sistema['média'] >= 7:
    sistema['situação'] = 'Aprovado'
elif 5 <= sistema['média'] < 7:
    sistema['situação'] = 'Recuperação'
else:
    sistema['situação'] = 'Reprovado'
print('-='*30)
for k,v in sistema.items():
    print(f'-O {k} é igual a {v}')
