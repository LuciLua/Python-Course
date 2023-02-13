"""
_____Tipo numerico_____

// ou / => divisão

number1 // number2 => retorna valor inteiro
int( number1 / number1 ) => retorna valor inteiro
number1 % number2 => módulo (retorna resto da divisao)

% => Modulo/'resto'

[ ! ] => T0do resto de divisão de um numero PAR por 2 dá 0
[ ! ] => T0do resto de divisão de um numero IMPAR por 2 dá 1

** => elevado

da pra somar assim tambem, ao passo de que atribui o valor
numero1 += numero2 => mesmo que => numero1 = numero1 + numero2
=> n1 *= n2 |  n1 -= n2 | n1 += n2 | n1 /= n2 | n1 //= n2

Funcao type diz o tipo
=> type(num1)

funcao __add__() adiciona valor ao num1
=> num1.__add__(2)

"""
print(f"Resto de: 10 / 2 = {10 % 2}")
print(f"Resto de: 11 / 2 = {11 % 2}")
print(f"Elevado: 11 ** 2 = {10 ** 2}")


print(f"Numero grande de facil leitura {1_000_000}")

num1 = 3
num2 = 10
num1 += num2
print(f'{num1} += {num2} = {num1}')
print(f'type de {num1} => {type(num1)}')



