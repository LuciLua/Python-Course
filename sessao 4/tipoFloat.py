"""
_____Tipo float_____
tipo real, decimal
Obs.: O separador de casas decimais na programcao é o . e nao a ,

[ ! ] - Ao converter valores float para inteiros, perde-se precisão

podemos trabalhar numveros complexos
\\ print(type(5j))

"""
# faz cast, transforma em tupla
valorErrado = 2,0
valorCerto = 2.2

print(f' {valorErrado} => type: {type(valorErrado)}')
print(f' {valorCerto} => type: {type(valorCerto)}')

# é possivel: dupla atribuiçao
valor1, valor2 = 1, 3
print(f'dupla atribuicao (esses sao tipos inteiros) => '
      f'valor1: {valor1} valor2: {valor2}')


def soma(n1, n2):
    print(f'{n1 + n2} => {type(n1 + n2)}')


soma(2.2, 2.8)

print(type(5j))

# Float para Inteiro
print(int(2.2))
# Inteiro para Float
print(float(2))


