# Propostas de melhoria para a linguagem python
# Import this

"""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

# ideia da PEP8: escrever codigos python de forma pythonica (de forma agradavel)

[1] - Utilizar camel case para nomes de classes
ex.: 
class CalculadoraCientifica:
    pass
    
[2] - Utilizar nomes em minuscula, separados por underline para funcoes ou variaveis
ex.:

def sum()
    pass
    
def sum_two():
    pass

numero_impar = 3

[3] - !!! Utilizar 4 espaçoes para a identação !!!

if 'a' in 'abc':
    print('tem quatro espaços aqui')
    
[4] - Separar funcoes e definicoes de classe com duas linhas em branco
    - MEtodos dentro de uma classe devem ser separados com uma unica linha em branco
    
[5] - Imports sempre devem ser feitos em linhas separadas
ex.:
import os

não tem problema em utilizar:
from types import StringType, ListType

Mas caso tenham muitos imports de um mesmo pacote:
from types import {
    StringType,
    ListType,
    SetType
}

Imports devem ser colocados no topo do arquivo, 
depois de comentarios ou docstrings e antes de constantes e variaveis globais

[6] - Nao dar espaçoes sem sentido (ex.: funcao( algo ); algo (1); x  =  1 )

[7] - Termina sempre uma instrucao com uma nova linha
"""

import os

print("os.name: ", os.name)


class CalculadoraCientifica:
    pass


banana_yellow = 'banana_yellow'

print(banana_yellow)
