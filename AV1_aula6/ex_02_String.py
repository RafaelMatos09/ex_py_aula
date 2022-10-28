"""
Nome ao contrário em maiúsculas.

# https://pt.stackoverflow.com/questions/379901/como-transformar-letras-mai%C3%BAsculas-em-min%C3%BAsculas-e-min%C3%BAsculas-em-mai%C3%BAsculas-no-p
# Função retorna string Maiuscula invertida

def reverter(string):
   retorno = ''
   for caractere in string:
      if caractere.isupper():
         retorno += caractere.lower()
      else:
         retorno += caractere.upper()
   return retorno[::-1]

reverter('rafael')
"""

# Função retorna string Maiuscula invertida
string = input('Digite a PALAVRA: ')

retorno = ''

for caractere in string:
      if caractere.isupper():
         retorno += caractere.lower()
      else:
         retorno += caractere.upper()
   
print(retorno[::-1])