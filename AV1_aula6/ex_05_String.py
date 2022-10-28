"""

    num_rows = int(input("Enter the number of rows"));
k = 1
for i in range(0, num_rows):
    for j in range(0, k):
        print("* ", end="")
    k = k + 1
    print()

    # Exemplo 1
# Nome na vertical em escada invertida. Altere o 
# programa anterior de modo que a escada seja invertida.



# Variavel usada como contador
k = 1
for i in range(0, 5):  # range de 0 a 5 para exibir 5 linhas
    for j in range(0, k): # adiciona o valor na coluna de posição k 
        if k == 6:
            print('f', end="") # A cada condição ele imprime a palavra de acordo com a linha
        if k == 5:
            print('fu', end="")
        if k == 4:
            print('ful', end="")
        if k == 3:
            print('fula', end="")
        if k == 2:
            print('fulan', end="")
        if k == 1:
            print('fulano', end="")

        
        k = k + 1
        print() # exibe cada linha e valores em cada repetição



"""
# Nome na vertical em escada invertida. Altere o 
# programa anterior de modo que a escada seja invertida.


# Exemplo 2

#entrada de dados
print("Nome na vertical em escada invertida")
nome = input("Digite o nome:")
#processamento
# Recebe o tamanho do nome
tamanho_nome = len(nome)
contador = tamanho_nome
#saída de dados
while(contador > 0):
    print(nome[0:contador])
    contador = contador - 1