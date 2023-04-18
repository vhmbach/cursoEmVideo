print('GERADOR DE PROGRESSÃO ARITMETICA')
print('-=' * 16)
c = 0
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
total = n

while c < 10:
    print(total, end='')
    if c<9:
        print(' -> ', end='')
    else:
        print('->', end='FIM')
    total += r
    c+=1