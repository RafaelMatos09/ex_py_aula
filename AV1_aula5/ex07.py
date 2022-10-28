"""
Aluno: Rafael Moreira Matos  
Matrícula: 202209201907 
Unidade: Maracanã
"""

# 7) Faça um Programa que leia três números e mostre o maior e o menor deles.

# Entrada de dados:

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

# Processamento e saida:
if num1 > num2 and num1 > num3:
    print('Primeiro numero é o maior')
elif num2 > num1 and num2 > num3:
    print('Segundo numero é o maior')
else:
    print('Terceiro numero é o maior')