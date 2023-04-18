a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('As retas podem formar um triângulo')
    if a == b == c:
        print('O triângulo formado é Equilátero.')
    elif a == b != c or a == c != b or b == c != a:
        print('O triângulo formado é Isóceles.')
    elif a != b != c:
        print('O triângulo formado é Escaleno.')
else:
    print('As retas não podem formar um triângulo.')