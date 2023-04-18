larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
tinta = 2
needed = area / tinta
print (f'A quantidade de tinta necessária para pintar uma parede de {area:.2f}mt² é {needed:.2f} lts.')
