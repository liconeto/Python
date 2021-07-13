from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \034[1;36m Desafio 083 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[32m Validador de expressões \033[m'
print(f'{texto2:*^50}')

expressao = []
parenteses = []
colchetes = []
chaves = []
expressao= str(input('Digite a expressão :')).strip()
for c in expressao:
    print(f'{c}')
    if '(' == c or c == ')':
        parenteses.append(c)
    #if '[' == c or c == ']':
    #    colchetes.append(c)
    #if '{' == c or c == '}':
    #    chaves.append(c)
print(f'A expressão digitada foi : {expressao}')
print(f'{parenteses}, {len(parenteses)}')
print(f'{colchetes}')
print(f'{chaves}')