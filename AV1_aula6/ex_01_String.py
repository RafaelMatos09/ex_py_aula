def Stam(x, y):
    '''
    Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
     Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo
    '''
    #x = input('Digite a primeira String: ')
    #y = input('Digite a segunda String: ')
   
    print(f'Tamanho de {x}:', len(x))
    print(f'Tamanho de {y}:', len(y))

    if len(x) == len(y):
        print('As duas strings são de tamanhos iguais.')
    else:
        print('As duas strings são de tamanhos diferentes.')

    if x == y:
        print('As duas strings possuem conteúdo iguais.')
    else:
        print('As duas strings possuem conteúdo diferente.')

    return ('FIM')

print(Stam('Brasil Hexa 2006','Brasil! Hexa 2006!'))

# Exemplo 2

#entrada de dados
print('Compara duas strings')
frase1 = input('digite a primeira frase: ')
frase2 = input('digite a segunda frase: ')
#processamento
tamanho1 = len(frase1)
tamanho2 = len(frase2)
if (tamanho1 == tamanho2):
    mensagem1 = 'As duas strings são de tamanhos iguais.'
else:
    mensagem1 = 'As duas strings são de tamanhos diferentes.'
if (frase1 == frase2):
    mensagem2 = 'As duas strings são de conteúdos iguais.'
else:
    mensagem2 = 'As duas strings são de conteúdos diferentes.'
#saída de dados
print('String 1: ' + frase1)
print('String 2: ' + frase2)
print('Tamanho de "' + frase1 + '": ' + str(tamanho1) + ' caracteres')
print('Tamanho de "' + frase2 + '": ' + str(tamanho2) + ' caracteres')
print(mensagem1)
print(mensagem2)