from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint
from operator import itemgetter

texto = ' \033[1;35m Desafio 102 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[34m Função Fatorial melhorado \033[m '
print(f'{texto2:*^50}')

def fatorial(num =1, show=None):
    f =1
    for c in range(num, 0, -1):
        if show == True:
            print(f'{c} ', end='')
        f *= c
    return f

while True:
    try:
        fat = int(input('O fatirial de que número? :'))
    except:
        print('Valor inválido, favor informar um número inteiro!')
    else:
        break
while True:
    try:
        ver = str(input('Quer ver ? [S/N] :')).upper()[0]
    except:
        print('valor inválido, Digite [S/N]')
    else:
        break
if ver == 'S':
    ver =True
else:
    ver=False
print(f': {fatorial(fat, show=ver)}')