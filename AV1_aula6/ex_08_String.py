"""
Palíndromo
"""

frase = input('Digite uma frase: ')
tam_frase = len(frase)
if frase[::-1] == frase[:]:
    print('palindromo')
else:
    print('nao é palindromo')

print(frase[::-1])