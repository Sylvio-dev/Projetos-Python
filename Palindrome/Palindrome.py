#!/usr/bin/env python3
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}'.format(junto, inverso))
if inverso == junto:
    print(f'A frase {frase} É UM PALÍNDROMO')
else:
    print('A frase digitada não é um palíndrome')
