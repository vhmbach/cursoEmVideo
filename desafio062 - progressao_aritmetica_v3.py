from time import sleep


n = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
total = 0
count = 0
mais = 10
while mais != 0:
    total += mais
    while count < total:
        print(f'{n} -> ', end="")
        n += razao
        count += 1
    print('PAUSA')
    mais = int(input('Quantos números mais deseja mostrar? '))
sleep(1)    
print('Fim da execução!')