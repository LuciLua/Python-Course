"""
_____O Tipo Booleano_____

Vem da algebra booleana, criada por George Boole

2 constantes = True or False
[ ! ] - Sempre com a inicial maiúscula

# Para operacoes basicas
 => Negacao: (Not) => se for falso, o resultado é verdadeiro,
  se for verdadeiro o resultado será falso
=> Ou: (or) => é uma operacoes binaria, ou seja: depende
de dois valores, ou um ou outro deve ser verdadeiro
    True or True => True
    True or False => True
    False or True => True
    False or False => False

=> e: (and) => também é uma operacao binaria (depende de 2 valores)
ambos os valores devem ser verdadeiros
    True and True => True
    True and False => False
    False and True => False
    False and False => False

"""

active_user = False
print(f'active_user: {active_user}')

# not
if not active_user:
    print("Usuario nao ativo")
else:
    print("Usuario ativo")

# or

logado = True

if active_user and logado:
    print("Usuario logado e ativo")
else:
    print("Usuario nao ativo e/ou nao logado")




