n = int(input('Digite a quantidade de termos que deseja exibir: '))
t1 = 0
t2 = 1
i = 0
while i < n:
    print(t1, end=' -> ')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    i += 1
print('FIM')