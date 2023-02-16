"""
Escopo de variaveis

dois casos de escopo

1 - Variaveis Globais
    => Seu escopo compreende td o programa
2 - Variaveis Locais
    => Sao reconhecidas apenas no bloco onde foram declaradas, seue scopo
    está limitado ao bloco onde foi declarada

Para declarar variaveis em python:
nome_da_variavel = valor_da_variavel


[ ! ] - Python é uma linguagem de tipagem dinamica, singifica que ao declararmos uma variavel
nao colocamos o tipo de dado dela. Este tipo é inferido ao atribuirmos o valor à mesma

Exemplo em C:
int numero = 42

(em linguagens tipadas nao da para fazer reatribuição, ou seja:
atribuir valores tipo string para ja definidos como variaveis que recebem
tipo number por exemplo)

em python, é possivel reatribuir valores
"""
# Exemplo de variavel global
nome_da_variavel = 42

print(type(nome_da_variavel))


if nome_da_variavel > 10:
    # novo é uma variavel local, se numero for menor do que 10, novo
    # nunca vai existir e nao podera ser chamado globalmente
    novo = nome_da_variavel + 10
    print(novo)


