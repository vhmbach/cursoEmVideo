n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

if n1 > n2:
    print(f'O primeiro valor é maior')
elif n2 > n1:
    print(f'O segundo valor é maior')
else:
    print('Não exite valor maior, os dois são iguais.')
