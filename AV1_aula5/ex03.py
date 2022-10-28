"""
Aluno: Rafael Moreira Matos  
Matrícula: 202209201907 
Unidade: Maracanã
"""

# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

# Entrada de dados:
letra = input("Digite 'F' para Feminimo e 'M' para Masculino: " )

# Processamento e saida:
if letra == 'F':
    print('F - Feminino')
elif letra == 'M':
    print('M - Masculino')
else:
    print('Sexo Inválido')