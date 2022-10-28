"""
analise o programa abaixo e, para cada uma das saídas (comandos print), detalhe passo a passo
como o Python (segundo suas prioridades) resolveria as equações e o resultado final obtido.
x=2
y=3
z = 0.5
print(x + x * x ** (y * x) / z)
print(not x + z < y or x + x * z >= y and True)

"""


x=2
y=3
z = 0.5
print(x + x * x ** (y * x) / z)
print(not x + z < y or x + x * z >= y and True)

# apos o resultado da operação, ele imprime a negação(reverte True para False) da codição x + z < y ou x + x * z >= y ,  
# nessa condição not que nao seja menor q y ou que nao seja maior igual que y retorna True