from math import cos, tan , sin, radians
num = float(input('Digite o angulo: '))
print(f'O seno de {num}° é: {sin(radians(num)):.2f} \n'
      f'O cosseno é: {cos(radians(num)):.2f} \n'
      f'A tangente é: {tan(radians(num)):.2f}')
