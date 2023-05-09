from Lib.interface import *
from time import sleep
while True:
    resposta = menu(['Cadastrar nova pessoa', 'Ver pessoas cadastradas', 'Sair do sistema'])
    if resposta == 1:
        cadastrarPessoa('Digite o nome que deseja cadastrar: ')
        print('Cadastro efetuado com sucesso!')
        sleep(2)
    elif resposta == 2:
        listarPessoas()
        sleep(3)
    elif resposta == 3:
        sairSistema()
        break
    else:
        print(f'\033[0;31mErro. Digite uma opção válida.\033[m')
        sleep(1.5)
print('Fim da execução!')