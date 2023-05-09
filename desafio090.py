alunos = dict()
alunos['nome'] = str(input('Digite o nome do aluno: '))
alunos['media'] = float(input(f'Média de {alunos["nome"]}'))
if alunos['media'] < 6:
    print(f'Nome é igual a {alunos["nome"]}')
    print(f'Média é igual a {alunos["media"]}')
    print(f'Situação é igual a Reprovado')
else:
    print(f'Nome é igual a {alunos["nome"]}')
    print(f'Média é igual a {alunos["media"]}')
    print(f'Situação é igual a Aprovado')
