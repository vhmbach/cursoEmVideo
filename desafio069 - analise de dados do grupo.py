pessoas = 0
maior = 0
homens = 0
mulher = 0
while True:
    print('=' * 20)
    print('CADASTRE UMA PESSOA')
    print('=' * 20)
    
    genero = str(input('Informe o gênero[M - Masculino | F - Feminino]: '))
    idade = int(input('Informe a idade: '))
    
    if genero in 'Mm':
        homens += 1
    elif genero == 'Ff':
        if idade < 20:
            mulher += 1    
    if idade > 18:
        maior += 1
    pessoas += 1
    opcao = str(input('Deseja continuar[S/N]? '))
    if opcao in 'Nn':
        break
print(f'Foram cadastradas {pessoas} pessoas, entre elas, {maior} têm mais de 18 anos, {homens} são homens e {mulher} são mulheres com menos de 20 anos.')