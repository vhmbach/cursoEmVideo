d = int(input('O veículo foi alugado por quantos dias?: '))
km = float(input('Quantos KM foram rodados com o veículo?: '))
vTotal = (d * 60) + (km * 0.15)
print(f'O valor total a pagar pelo aluguel do veículo é R${vTotal:.2f}')
