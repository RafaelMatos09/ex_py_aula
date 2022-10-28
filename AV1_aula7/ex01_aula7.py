'''Aula07_exercicio01.py
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
    a."Telefonou para a vítima?"
    b."Esteve no local do crime?"
    c."Mora perto da vítima?"
    d."Devia para a vítima?"
    e."Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ele será classificado como "Inocente".
'''
# armazenar quantidade resultado positivo.
quantidade_positivo = 0

# status da resposta.
status = {2: "Suspeito(a)", # chave:valor
        3: "Cúmplice",
        4: "Cúmplice",
        5: "Assassino"}

# armazenar uma lista de perguntas.
lista_perguntas = ("Telefonou para a vítima?",
                "Esteve no local do crime?",
                "Mora perto da vítima?",
                "Devia para a vítima?",
                "Já trabalhou com a vítima?")

# fazer as perguntas.
for i in range(0,len(lista_perguntas)):
# efetuar a pergunta.
    print(lista_perguntas[i] + " (digite sim ou não).")
# Obter uma resposta.
    resposta = input("Resposta: ")
# Analisar a resposta e se for positivo incrementar o valor
    if resposta.lower() == "sim":
# incrementar mais um.
        quantidade_positivo += 1
# Verificar compatibilidade dos dados com o status.
    if quantidade_positivo in status:
# Titular o status da pessoa.
        print(status[quantidade_positivo])
    else:
        print("Inocente")