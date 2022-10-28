"""
Data por extenso


date_time_str = input('Digite a data de nascimento: 001100')

date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y')


print ("The type of the date is now",  type(date_time_obj))
print ("The date is", date_time_obj)


"""
dia = int(input('Dia: '))
mes = int(input('Mes: '))
ano = int(input('Ano: '))

print(f'Data de Nascimento: {dia}/{mes}/{ano}')

if mes == 1:
    print(f' Você nasceu em {dia} de Janeiro de {ano}')
if mes == 2:
    print(f' Você nasceu em {dia} de Fevereiro de {ano}')
if mes == 3:
    print(f' Você nasceu em {dia} de Março de {ano}')
if mes == 4:
    print(f' Você nasceu em {dia} de Abril de {ano}')
if mes == 5:
    print(f' Você nasceu em {dia} de Maio de {ano}')
if mes == 6:
    print(f' Você nasceu em {dia} de Junho de {ano}')
if mes == 7:
    print(f' Você nasceu em {dia} de Julho de {ano}')
if mes == 8:
    print(f' Você nasceu em {dia} de Agosto de {ano}')
if mes == 9:
    print(f' Você nasceu em {dia} de Setembro de {ano}')
if mes == 10:
    print(f' Você nasceu em {dia} de Outubro de {ano}')
if mes == 11:
    print(f' Você nasceu em {dia} de Novembro de {ano}')
if mes == 12:
    print(f' Você nasceu em {dia} de Dezembro de {ano}')


