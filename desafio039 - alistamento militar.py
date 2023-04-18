from datetime import date
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - ano_nascimento
if idade < 18:
    print(f' Ainda faltam {18 - idade} ano(s) para você se alistar!')
elif idade == 18:
    print('Você já está no período de alistamento!')
else:
    print(f'Já passaram {idade - 18} ano(s) do periodo de alistamento!')
    