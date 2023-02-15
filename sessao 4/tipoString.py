"""
considerado string:
->  estiver entre aspas
(simples, duplas, simples triplas, duplas triplas)

# Split => transforma em uma lista de strings
    => variavel[0:4] => posicao 0 ate 4 (slice de string)

# comecar do primeiro elemento
# ir ate ultimo elemento
# e inverta:
print(f'{split_this_phase[::-1]}')
"""

print('sou uma string')
print("sou uma string")
print('''sou uma string''')
print("""sou uma string""")


name = 'angeliNA\nJOLIE'
bio = """Eu sou 
uma pessoa"""
split_this_phase = "esta é uma frase esplitada legal"

print(f'Name: {name.title()}\nBio: {bio.lower()}')
print(f'Frase: {split_this_phase.split()}')

print(f'{split_this_phase[0:10]}')
print(f'{split_this_phase.split()[3:4]}')
print(f'{split_this_phase.split()[4]}')

# invertertendo string
print(f'{split_this_phase[::-1]}')
print(f'{split_this_phase[::1]}')

# replace
print(f"{split_this_phase.replace('legal', 'awesome')}")

texto = 'socorram me subino onibus em marrocos'
print(f'Palíndromo: {texto[::-1]} = {texto}')



