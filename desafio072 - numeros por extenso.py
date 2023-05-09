numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Desesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    opcao = int(input('Digite um número entre 0 e 20: '))
    if opcao < 0 or opcao > 20:
        opcao = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        print(f'Você digitou {numeros[opcao]}')
        break