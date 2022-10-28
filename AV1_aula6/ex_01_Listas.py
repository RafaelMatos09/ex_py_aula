"""
Faça um Programa que leia um vetor 
de 5 números inteiros e mostre-os.
"""
#variável
listaNumeros = []
#entrada de dados
print ('Informe os 5 números')
for i in range(5):
    numero = int(input('Digite um número inteiro: '))
# processamento
    listaNumeros.append(numero)

#saída de dados
print (listaNumeros)