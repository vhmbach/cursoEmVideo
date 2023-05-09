def leiaDinheiro(v):
    while True:
        if v != type(v) != float:
            print(f'\33[31m {v} é um preço inválido!\33[m')
            print(type(v))
            v = input('Digite o preço: ')
        else:
            break
    return v
