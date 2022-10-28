"""
Faça um Programa que peça as quatro notas de 10 alunos, 
calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos 
com média maior ou igual a 7.0.

lista = []

x = 0

while x < 11:
    x = x + 1
    if x < 11:
       nota = float(input(f'Digite a nota {x} '))
    lista.append(nota)

aprov = []

for i in lista:
     if i >= 7:
        aprov.append(i)
    
print(f' Numero de alunos aprovados: {len(aprov)-1}')
"""

#Exemplo 2

#variável
listaNotas = [] # recebe media de notas
soma = 0 
numeroAlunos = 0 # recebe numero de alunos aprovado
numeroAlunosReprovados = 0 # recebe numero de alunos reprovados
#entrada de dados
print ('Notas dos Alunos')
for i in range(3):
    soma = 0 # recebe soma de notaAluno 
    notasAluno = []
    print ('Aluno: ' + str(i+1)) # exibe qual aluno de acordo com a linha
    for j in range(4): # repetiçao de colunas na matriz 4 notas
        nota = float(input('Digite a nota: ')) # solicita nota
        notasAluno.append(nota) # atribui nota a notasAluno
        #processamento
        soma += notasAluno[j] # soma notasAluno
    media = soma/4  # calcula a media e atribui a variavel media
    listaNotas.append(media) # atribui media a listaNotas
    if (media >=7):
        numeroAlunos += 1 # atribui ao contador numeroAlunos + 1
    else:
        numeroAlunosReprovados += 1 # atribui ao contador numeroAlunosReprovados + 1
#saída de dados
print (listaNotas)
print('Alunos com média >= 7: ',numeroAlunos)
print('Alunos com média < 7: ',numeroAlunosReprovados)