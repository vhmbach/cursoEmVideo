from time import sleep


print('=' * 18)
print('SISTEMA DE CALCULO')
print('=' * 18)

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
def menu():
      print('=' * 18)
      print('MENU DE OPÇÕES')
      print('''[1] - SOMAR
[2] - MULTIPLICAR
[3] - MAIOR
[4] - TROCAR NÚMEROS
[5] - SAIR
      ''')
menu()
opcao = 0

while opcao == 0:
    opcao = int(input('Escolha uma opção: '))
    sleep(1)
    if opcao == 1:
          soma = n1 + n2
          print(f'{n1} mais {n2} é igual a: {soma}')
          opcao = 0
          print()
          sleep(2)
          menu()
    elif opcao == 2:
          mult = n1 * n2
          print(f'{n1} multiplicado por {n2} é igual a: {mult}')
          print()
          sleep(2)
          opcao = 0
          menu()
    elif opcao == 3:
          if n1 > n2:
                print(f'\33[32m{n1}\33[m é maior que \33[32m{n2}\33[m.')
          elif n1 < n2:
                print(f'\33[32m{n2}\33[m é maior que \33[32m{n1}\33[m.')
          else:
                print('O valores digitais são iguais')
          sleep(2)
          opcao = 0
          menu()
    elif opcao == 4:
          n1 = float(input('Digite o primeiro número: '))
          n2 = float(input('Digite o segundo número: '))
          opcao = 0
          menu()
    elif opcao == 5:
          print('FIM DE EXECUÇÃO DO PROGRAMA')
    else:
          print('Digite uma opção válida!!')
          print()
          opcao = 0
          menu()