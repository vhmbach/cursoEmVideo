teste = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')), int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')))
if 9 in teste:
    print(f'O número 9 apareceu {teste.count(9)} vezes.')
else:
    print(f'O número 9 não foi digitado.')
if 3 in teste:
    print(f'O número 3 apareceu na posição {(teste.index(3) + 1)}')
else:
    print(f'O número 3 não foi digitado.')
print('Os números pares digitados foram', end=' ')
for numero in teste:
    if numero % 2 ==0:
        print(numero, end=' ')
