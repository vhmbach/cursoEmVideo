from datetime import date
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
trabalhador['ano_nascimento'] = int(input('Ano de nascimento: '))
trabalhador['idade'] = date.today().year - trabalhador['ano_nascimento']
trabalhador['ctps'] = int(input('Número da Carteira de trabalho: '))
if trabalhador['ctps'] != 0:
    trabalhador['ano_contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: '))
tempo_servico = date.today().year - trabalhador['ano_contratacao']
aposentadoria = trabalhador['idade'] + (35 - tempo_servico)
for d in trabalhador:
    print(f'{d}: {trabalhador[d]}')
if trabalhador['ctps'] != 0:
    print(f'Idade que irá se aposentar: {aposentadoria}')