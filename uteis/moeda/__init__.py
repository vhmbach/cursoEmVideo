def acrescimo(v, p, form=True):
    porcentagem = v + (v * p / 100)
    if form:
        return moeda(porcentagem)
    else:
        return porcentagem


def desconto(v, p, form=True):
    porcentagem = v - (v * p / 100)
    if form:
        return moeda(porcentagem)
    else:
        return porcentagem


def dobro(v, form=True):
    dobra = v * 2
    if form:
        return moeda(dobra)
    else:
        return dobra


def metade(v, form=True):
    divide = v / 2
    if form:
        return moeda(divide)
    else:
        return divide


def moeda(v, cambio='R$'):
    valor = (f'{cambio}{v:.2f}'.replace('.', ','))
    return valor


def resumo(v, a, r):
    print('-' * 20)
    print(f'{"RESUMO DO VALOR":^20}')
    print('-' * 20)
    print(f'''valor com acréscimo de {a}% \t{acrescimo(v, a)}
valor após redução de {r}% \t{desconto(v, r)}
metade do valor \t\t\t{metade(v)}
dobro do valor \t\t\t\t{dobro(v)}''')
    return resumo
