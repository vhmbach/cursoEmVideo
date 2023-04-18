from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjascente: '))
hip = hypot(co, ca)
print(f'{hip:.2f}')
