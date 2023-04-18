n = int(input('Digite um número: '))
soma = n
maior = n
menor = n
cont = 1
while True:
    choice = str(input('Deseja continuar? ').lower().strip())
    if choice in 'não':
        break
    n = int(input('Digite mais um número: '))
    soma += n
    cont += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
media = soma / cont
print(f'Você digitou {cont} números. A soma dos números digitados foi {soma}')
print(f'O menor número digitado foi {menor} e o maior foi {maior}.')
print(f'A média dos números digitados é igual a {media}.')