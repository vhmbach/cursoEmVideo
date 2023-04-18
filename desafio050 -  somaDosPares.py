
soma=0
for i in range(0, 6):
    i = int(input('Digite um número inteiro: '))
    if i % 2 == 0:
        soma += i    
print(f'A soma dos numeros pares digitados é igual a {soma}')