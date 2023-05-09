palavras = ('carro', 'computador', 'bicicleta', 'notebook', 'cachorro', 'pessoa', 'python')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra.upper(), end=' ')


palavras_teste = [palavra for palavra in palavras]
letras_teste = [letra for letra in palavras_teste if letra in 'aeiou']

print(f'palavras_teste {palavras_teste}')