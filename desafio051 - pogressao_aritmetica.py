t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
soma = t
print(soma)
for i in range (0, 10):
    soma += r
    print(soma, end=' -> ')
print('END')