n = int(input('Digite um número: '))
soma = 0
count = n
total = 0
while count != 999:
    soma += n
    total += 1
    n = int(input('Digite mais um número: '))
    count = n
print(f'Foram digitados um total de {total} números, e a soma entre eles é {soma}')