"""
Conta espaços e vogais. Dado uma string com uma frase informada 
pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
"""

frase = input('Digite uma frase: ')

cont_vogal = 0
cont_space = 0

for letra in frase:
    
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        cont_vogal += 1
    if letra == ' ':
        cont_space += 1

print(f'Tem {cont_space} espaços em branco e {cont_vogal} vogais. ')
