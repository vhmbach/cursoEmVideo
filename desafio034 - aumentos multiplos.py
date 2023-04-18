n = float(input('Digite o valor salário: '))
if n <= 1250.0:
    aumento = 15/100 * n + n
    print(f'O salário com o aumento de 15% passará a ser R${aumento:.2f}')
else:
    aumento = 10/100 * n + n
    print(f'O salário com o aumento de 10% passará a ser R${aumento:.2f}')
