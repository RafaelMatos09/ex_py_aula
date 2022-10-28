"""
Aluno: Rafael Moreira Matos  
Matrícula: 202209201907 
Unidade: Maracanã

1) Faça um programa Python que calcule a área do cubo.

"""


def area_cubo(l):
    a = 6 * (l * l)
    return a

# Entrada de dados:
lado = float(input('Informe o tamanho do lado: '))
cubo = area_cubo(lado)
#processamento e saida:
print('Area do cubo %.2f ' % cubo)