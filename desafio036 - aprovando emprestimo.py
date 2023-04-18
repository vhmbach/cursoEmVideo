print('-='*12)
print(' SISTEMA DE EMPRESTIMO')
print('-='*12)

salario = float(input('Digite o valor do salário: '))
valor_imovel = float(input('Digite o valor do imóvel: '))
anos = int(input('Em quantos anos deseja pagar?:  '))
valor_prestacao = valor_imovel / (anos*12)

if valor_prestacao <= salario * 30 / 100:
    print('EMPRÉSTIMO APROVADO!!')
    print(f'O valor da prestação será de R${valor_prestacao:.2f} mensais.')
else:
    print('EMPRÉSTIMO NEGADO!!')
    print(f'Valor da prestação: R${valor_prestacao:.2f} \n'
          f'Para o emprétimo ser aprovado, o valor da prestação precisa ser de no máximo R${salario * 30 / 100:.2f}')
    