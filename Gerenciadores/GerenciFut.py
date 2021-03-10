#Aqui temos um gerenciador para um técnico por exemplo, para avaliar o jogador com maior aproveitamento (;
#!/usr/bin/env python3
time = list()
dados = dict()
partidas = list()
while True:
    dados.clear()
    dados ['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {dados["nome"]} jogou ?'))
    partidas.clear()
    for p in range(tot):
        partidas.append(int(input(f'Quantos gols na partida {p+1}: ')))
    dados['gols'] = partidas [:]
    dados ['total'] = sum(partidas)
    time.append(dados.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N')
    if resp == 'N':
        break
print('=-'*30)
print('cod ',end='')
for i in dados.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
for k,v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador ? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO do JOGADOR {time[busca]["nome"]}')
        for i,g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('=-'*30)
print('<<< VOLTE SEMPRE >>>')
