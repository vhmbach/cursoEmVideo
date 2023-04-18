valor_produto = float(input('Insira o valor do produto: '))
print('\n')
print('Qual é a forma de pagamento?: ')
print('*'*19)
print('1 - DINHEIRO/CHEQUE \n'
      '2 - CARTÃO')
print('*'*19)
opcao = int(input('ESCOLHA UMA OPÇÃO: '))
print('\n')
if opcao == 1:
    print(f'O produto no valor de R${valor_produto:.2f} tem 10% de desconto ao pagar com dinheiro/cheque. \n'
          f'O valor do produto com o desconto passa a ser de R${valor_produto - (valor_produto * 10 / 100):.2f}')
elif opcao == 2:
    opcao = int(input('Em quantas parcelas deseja comprar?: '))
    print('\n')
    if opcao == 1:
        print(f'O produto no valor de R${valor_produto:.2f} tem 5% de desconto ao pagar a vista no cartão. \n'
          f'O valor do produto com o desconto passa a ser de R${valor_produto - (valor_produto * 5 / 100):.2f}')
    elif opcao == 2:
        print(f'O valor do produto é de R${valor_produto:.2f} \n'
          f'O pagamento ficará em {opcao} parcelas de R${valor_produto / opcao:.2f}')
    else:
        print(f'O produto no valor de R${valor_produto:.2f} tem 20% de juros ao parcelar em {opcao}x. \n'
          f'O valor do produto com o acrescimo passa a ser de R${valor_produto + (valor_produto * 20 / 100):.2f} \n'
          f'O pagamento ficará em {opcao} parcelas de R${(valor_produto + (valor_produto * 20 / 100)) / opcao:.2f}')
print('\n')
        