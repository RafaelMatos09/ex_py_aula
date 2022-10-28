"""
Aluno: Rafael Moreira Matos  
Matrícula: 202209201907 
Unidade: Maracanã
"""

# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o
# valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# Entrada de dados:

num = int(input('Digite uma nota de 0 a 10: '))

# Saida de dados e processamento:

# Estrutura de repetição
while num > 10 or num < 0:
    if num > 10 or num < 0:
        print('Numero invalido')

    num = int(input('Digite uma nota de 0 a 10: '))
