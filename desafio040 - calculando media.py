n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'Média: {media:.1f} \n'
          f'REPROVADO')
elif media >= 5 and media <= 6.9:
    print(f'Média: {media:.1f} \n' 
          f'RECUPERAÇÃO')
else:
    print(f'Média: {media:.1f} \n'
          f'APROVADO')