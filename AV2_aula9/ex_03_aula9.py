"""
Escreva um programa que recebe três inteiros como entrada do teclado e exiba na tela a
média, a soma, o produto, o menor valor e o maior valor, usando uma linha para cada
resultado.


# Exemplo 1
# Entrada de dados
#x = list(map(int, input("Digite os 3 valores na mesma linha: ").split()))
x = input('Digite os 3 valores na mesma linha: ').split()
num1, num2, num3 = x

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

# Processamento
media = (num1 + num2 + num3) / 3
soma = num1 + num2 + num3
produto = num1 * num2 * num3

# Saida de dados
print('Media: %0.2f' % media)
print('Soma: %i' % soma)
print('Produto: %i' % produto)

# Processamento e saida de dados
if num1 > num2 and num1 > num3:
    print('num1 maior numero')
if num2 > num1 and num2 > num3:
    print('num2 maior numero')
if num3 > num1 and num3 > num2:
    print('num3 maior numero')

print(type(media))
print(type(soma))
print(type(produto))
"""

def calc_med(*args):
    """
    Calcula média de notas, podendo utilizar quantas notas precisar.
    """
    a = sum(args) / len(args)
    return a

def calc_soma(*args):
    """
    Calcula soma de notas, podendo utilizar quantas notas precisar.
    """
    a = sum(args)
    return a

def calc_produto(x, y, z):
    """
    Calcula produto de 3 notas
    """
    a = x * y * z
    return a


# Entrada de dados:
v = input('Digite as notas: nota1 nota2 nota3  etc...<- dessa forma').split() # Transforma a entrada de string em uma lista

num1, num2, num3 = v  # Desempacotando uma lista em varias variaveis

# Processamento:
num1 = int(num1) # Convertendo string em inteiro
num2 = int(num2)
num3 = int(num3)
media = calc_med(num1, num2, num3)# Com o parâmetro *args posso utilizar quantos argumentos precisar
soma = calc_soma(num1, num2, num3)
produto = calc_produto(num1, num2, num3)

# Saida de dados:
print(f'Media: {media}')
print(type(media))
print(f'Soma: {soma}')
print(f'Produto: {produto}')
print(f'Menor valor: {min(media,soma,produto)}')
print(f'Maior valor: {max(media,soma,produto)}')
