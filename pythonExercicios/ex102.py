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

def fatorial(num =1, show=False):
    """
    ->Calcula do fatorial de um número indicado, com 2 parâmetros 'num' e 'show'
    obeservar que os parâmetros são opcionais!
    :param num: número inteiro qual será calculado o fatorial.
    :param show: valor booleano 'True | False' sendo opicional para mostra ou não a etapa de calculo.
    :return: o fatorial do parâmetro num
    """
    f =1
    for c in range(num, 0, -1):
        if show == True :
            print(f'\033[34m{c}\033[m ', end='')
            if c > 1:
                print('x ', end='')
        f *= c
    return f

while True:
    try:
        fat = int(input('O fatorial de que número? :'))
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
print(f'{help(fatorial)}')
print(f'= \033[1;31m{fatorial(fat, show=ver)}\033[m')