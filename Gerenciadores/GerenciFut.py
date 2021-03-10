#Aqui temos um gerenciador para um técnico por exemplo, para avaliar o jogador com maior aproveitamento (;
#!/usr/bin/env python3
dados = dict()
partidas = list()
dados ['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {dados["nome"]} jogou ?'))
for p in range(tot):
    partidas.append(int(input(f'Quantos gols na partida {p+1}: ')))
dados['gols'] = partidas [:]
dados ['total'] = sum(partidas)
print('=-'*30)
print(dados)
print('=-'*30)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O jogador {dados["nome"]} jogou {tot} partidas')
for i,v in enumerate(dados['gols']):
    print(f'  =>Na partida {i+1} marcou {v} gols')
print(f'Foi um total de {dados["total"]} gols')
