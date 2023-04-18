sal = float(input('Digite o valor do salário: '))
adicional = (sal * 15) / 100
nSal = sal + adicional
print(f'O salário é R${sal:.2f}, com o aumento de 15% fica R${nSal:.2f}. \n' 
      f'Aumento de: R${adicional:.2f}.')
