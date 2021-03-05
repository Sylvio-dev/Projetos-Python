#!/usr/bin/env python3
print('{:=^40}'.format('LOJAS SYLVIOs S.A'))
preço = float (input ('Qual foi o valor das compras: R$'))
print ('''FORMAS DE PAGAMENTO
[ 1 ] Á vista dinheiro/cheque 10% de DESCONTO
[ 2 ] Á vista no cartão 5% de DESCONTO
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão (com juros)''')
opção = int(input('Qual opção você prefere ?'))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format (parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('São quantas parcelas ?'))
    parcela = total / totalparc
    print ('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preço
    print('\033[31mOPÇÃO DE PAGAMENTO INVÁLIDA. Tente novamente\033[m!')
print ('Sua compra de R${:.2f} no final vai custar R${:.2f}'.format(preço, total))
