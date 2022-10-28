"""
Aluno: Rafael Moreira Matos  
Matrícula: 202209201907 
Unidade: Maracanã

Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de
um item antes do imposto. A função "altera" o valor de custo para incluir o imposto sobre vendas. (0,5
ponto).
"""

def somaImposto(taxaImposto, custo):
    a = (taxaImposto/100)*custo
    b = a + custo
    return b

# Entrada de dados
imp = float(input('Digite a taxa: '))
cust = float(input('Digite o custo: '))

# Processamento e saida
calc = somaImposto(imp, cust)
print(f'Valor com imposto: {calc}')