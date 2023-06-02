"""
------ESTRUTURAS DE REPETICAO------

Loop:   estrutura de repetição
For:    é uma dessas estruturas de repetição

for item in interavel:
    // execucao do loop


Utilizamos loops para iterar sobre sequencias ou sobre valores iteráveis


Exemplos de iteraveis:

- Strings   "string"
- Listas    [1,2,3,4]
- Range     range(1,10)


"""


name = 'Luci Lua'
list = [1,3,5,7,9]
numbers = range(1,10)


print('-----1----')
# 1. Exemplo de for: in
for letra in name:
    print(letra)
    
print('-----2----')
# 2. Exemplo de for: iterando sobre uma lista
for number in list:
    print(number)

print('-----3----')
# 3. Exemplo de for: iterando sobre um range
for number in numbers:
    print(number)



