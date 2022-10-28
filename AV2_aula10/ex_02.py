"""
Aluno: Rafael Moreira Matos  
Matrícula: 202209201907 
Unidade: Maracanã

2 - Faça um programa que converta da notação de 24 horas para a notação 
de 12 horas.
"""


def converte_h(hour, min, ctime=' '):

    if hour > 12:
        a = hour - 12
        ctime = 'P.M'
    else:
        a = hour
        ctime = 'A.M'

    b = f'{a}:{min} {ctime}'
    return b


def imp_saida(s):
    a, b = s
    a = int(a)
    b = int(b)

    x = converte_h(a, b)
    return x


while True:

    v = input('Digite o horario para converter: ').split()

    z = imp_saida(v)

    print(z)

    y = input('Deseja continuar ? \n')

    if y.lower() == 'sim':
        v = input('Digite o horario para converter: ').split()
        z = imp_saida(v)
        print(z)
    else:
        break
