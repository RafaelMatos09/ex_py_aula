"""
Nome na vertical em escada. 
"""

nome = input('Digite o nome: ')

tamanho_nome = len(nome)
contador = tamanho_nome

while (contador >= 0):
    print(nome[contador:])
    contador = contador - 1