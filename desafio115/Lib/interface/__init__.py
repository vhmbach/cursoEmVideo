from time import sleep
def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt)
    print(linha())


def leiaInt(msg):
    while True:
        try:
            entrada = int(input(msg))
        except (ValueError, TypeError):
            print('Erro. Digite um valor inteiro válido')
            continue
        else:
            return entrada
            break


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1
    print(linha())
    opc = leiaInt('Escolha uma opção: ')
    return opc


def sairSistema():
    print(f'\033[0;33mSaindo do sistema\033[m', end='')
    sleep(0.7)
    print('.', end='')
    sleep(0.7)
    print('.', end='')
    sleep(0.7)
    print('.')
    sleep(1)


def cadastrarPessoa(entrada):
    with open('pessoas_cadastradas.txt', 'a', encoding='UTF-8') as arquivo:
        arquivo.write(input(entrada))
        arquivo.write('\n')


def listarPessoas():
    with open('pessoas_cadastradas.txt', 'r') as arquivo:
       nomes = arquivo.readlines()
       for nome in nomes:
           print(nome, end='')
           sleep(1)
