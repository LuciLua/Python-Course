# dir(__builting__) => recursos integrados da linguagem
# Recebendo dados do usuario:

# _____Entrada de dados_____
print("\u001b[33mQual seu nome? \u001b[0m")
name = input("\u001b[33mNome: \u001b[0m")
year = 2023

# _____Saida de dados_____
# Print mais 'antigo' (da versao 2.x):
print('\u001b[34m[antigo] \u001b[0m'
      'Seja bem-vindo(a) %s! Estamos em %s'
      % (name.title(), year))

# Print mais moderno (criado a partir da versao 3.x):
print("\u001b[32m[moderno] \u001b[0m"
      "Seja bem vindo(a) {0}! Estamos em {1}".format(name, year))

# Print da forma mais atual (a partir do 3.6 ou 3.7)
print(f'\u001b[32m[+moderno] \u001b[0m'
      f'Seja bem-vindo(a) {name}! Estamos em {year}')

age = 21
print(f'\u001b[32m[+moderno] \u001b[0m'
      f'Vamos somar (com cast) {age} + 4  = {int(age) + 4}')
# int(num) => cast
# Cast => conversao de um tipo de dado para outro
print(f'\u001b[32m[+moderno] \u001b[0m'
      f'Vamos somar (sem cast) {age} + 4  = {age + 4}')
"""

[ ! ] todo dado recebido via input() é do tipo string
[ ! ] String é tudo que tiver entre:
    - Aspas simples 'texto'
    - Aspas duplas "texto"
    - Aspas simples triplas '''texto'''
    - Aspas duplas triplas """  """
    
"""


