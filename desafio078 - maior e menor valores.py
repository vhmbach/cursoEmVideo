valores = list()
for valor in range(0,5):
    if valor == 0:
        valores.append(int(input('Digite um valor: ')))
    else:
        valores.append(int(input('Digite mais um valor: ')))
        
print(f'O menor valor digitado foi {min(valores)} nas posições ', end='')
for posicao, valor in enumerate(valores):
    if valor == min(valores):
        print(posicao, end='.. ')
print(f'\nO menor valor digitado foi {max(valores)} nas posições ', end='')
for posicao, valor in enumerate(valores):
    if valor == max(valores):
        print(posicao, end='.. ')