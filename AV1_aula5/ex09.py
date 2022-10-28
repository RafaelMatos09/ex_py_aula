"""
Aluno: Rafael Moreira Matos  
Matrícula: 202209201907 
Unidade: Maracanã
"""

# 9) Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.


# Exemplo 1

#print('Numero impares de 1 a 50:')
#num = 0
#for num in range(1, 51):
#    if num % 2 > 0:
#        print(num)
#print('FIM')        


 #Exemplo 2

# OBS: Nesse exemplo o valor de passo de 2 em 2 mostrando somente os 
# numeros impares, ramge(valor_de_inicio, valor_de_parada, passo)

print('Numero impares de 1 a 50:')

num = 0
for num in range(1, 51, 2):
    print(num)

print('FIM')