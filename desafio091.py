from random import randint
jogadores = {'jogador1':randint(1, 6), 'jogador2':randint(1, 6), 'jogador3':randint(1, 6), 'jogador4':randint(1, 6)}
print('VALORES SORTEADOS:')
for j in jogadores:
    print(j, jogadores[j])
print()
print('RANKING DOS JOGADORES:')
posicao = 1
for j in sorted(jogadores, key = jogadores.get, reverse=True):
    print(f'{posicao}º lugar: {j}, com {jogadores[j]}')
    posicao += 1