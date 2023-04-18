n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Digite mais um número: '))
#VERIFICANDO MENOR VALOR
menor = n1
if n2 < n1 and n2 < 3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
#VERIFICANDO MAIOR VALOR
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 >n2:
    maior = n3
print(f'O menor valor é {menor} e o maior valor é {maior}')
