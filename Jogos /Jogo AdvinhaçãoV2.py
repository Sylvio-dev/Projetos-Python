#!/usr/bin/env python3
import random
pc = random.randint(0,10)
print('Sou seu computador...')
print('Pensei em um número de 0 á 10')
print ('Você consegue advinhar ?')
acertou = False
tenta = 0
while not acertou:
    jogador = int(input(('Qual o seu palpite ?')))
    tenta += 1
    if jogador == pc:
        acertou = True
    elif jogador < pc:
        print ('Mais... Tente mais uma vez.')
    elif jogador > pc:
        print('Menos... Tente mais uma vez.')
print(f'Você acertou com {tenta} tentativas. Parabéns !')
