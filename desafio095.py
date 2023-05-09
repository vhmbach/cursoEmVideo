time = list()
jogador = dict()
partidas = list()
while True:
    jogador['nome'] = str(input('Nome: '))
    tot= int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for g in range(0, tot):
        partidas.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {g + 1}? ')))
        jogador['gols'] = partidas[:]
        jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    partidas.clear()
    tot = 0
    while True:
        escolha = str(input('Deseja continuar[S/N]?: ').upper())
        if escolha in 'SN':
            break
        print('Opção inválida!')
    if escolha in 'Nn':
        break
print('=-' * 25)
print('id', end=' ')
for i in jogador.keys():
    print(f'{str(i):<14}', end= ' ')
print()
for k, v in enumerate(time):
    print(f'{k:>2}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()