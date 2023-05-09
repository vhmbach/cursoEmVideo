from random import randint
cont = 0
print('=-' * 15)
print('JOGO PAR OU IMPAR')
print('=-' * 15)
while True:
    bot = randint(0, 10)
    player_choice = int(input('''Escolha:
[1] - PAR
[2] - IMPAR
'''))
    player_number = int(input('Digite um número de 0 a 10: '))
    result = player_number + bot
    if player_choice == 1 and result % 2 == 0:
        cont += 1
        print(f'Você escolheu {player_number} e o computador escolheu {bot}. A soma dos valores é PAR')
        print(f'Você Venceu! Vamos mais uma partida. ')
    elif player_choice == 1 and result % 2 != 0:
        print(f'Você escolheu {player_number} e o computador escolheu {bot}. A soma dos valores é IMPAR')
        print(f'VOCÊ PERDEU!')
        break
    elif player_choice == 2 and result % 2 != 0:
        cont += 1
        print(f'Você escolheu {player_number} e o computador escolheu {bot}. A soma dos valores é IMPAR')
        print(f'Você Venceu! Vamos mais uma partida. ')
    elif player_choice == 2 and result % 2 == 0:
        print(f'Você escolheu {player_number} e o computador escolheu {bot}. A soma dos valores é PAR')
        print(f'VOCÊ PERDEU!')
        break
print(f'Você venceu {cont} partidas seguidas.')
print('FIM DO JOGO!')