n1 = float(input('Digite o valor do produto: '))
desconto =(n1 * 5) / 100
nValor = n1 - desconto
print(f'O produto custa R${n1:.2f}, com o desconto fica R${nValor:.2f}. \n'
      f'Valor do desconto: R${desconto:.2f}')
