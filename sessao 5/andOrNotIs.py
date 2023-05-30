"""
Estruturas Lógicas:

- AND 
- OR
- NOT
- IS

Operadores unários: 
    -   not

Operadores binários: 
    -   and 
    -   or
    -   is

"""

# para AND os dois valores precisam ser True
ativo = False
logado = False

if ativo and logado:
    print("Bem-vindo user")
else:
    print("Você precisa ativar sua conta")
    
# para OR um ou outro valor precisa ser True
# para NOT o valor do boleano precisa ser invertido. Se for True vira False e se for False vira True

if not ativo:
    print("Você precisa ativar sua conta")
else:
    print("Sua conta está ativa")

# para IS o valor é comparado com o segundo valor

if logado is ativo:
    print("Logado É igual a ativo")
elif logado is not ativo:
    print("Logado NAO É igual a ativo")
    
    
print('aaa' is 'aaa')
