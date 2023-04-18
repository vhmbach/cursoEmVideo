n = int(input('Digite um número inteiro: '))
f = n - 1
total = 0
fatorial = n
print(f'A fatoração de {n} é igual a: {n}', end=(''))
while f != 0:
    fatorial *= f
    print(f'x{f}', end=(''))
    f = f -1
print(' =',fatorial)
    