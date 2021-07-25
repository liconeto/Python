from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint
from operator import itemgetter

texto = ' \033[1;36m Desafio 100 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[34m Função Sorteia e somaPar \033[m '
print(f'{texto2:*^50}')
valores = []
def sorteia():
    print('-=' * 30)
    print('Sorteando 5 valores da lista: ',end='')
    for c in range(0, 5):
        num = randint(0, 10)
        valores.append(num)
        sleep(0.4)
        print(f'\033[32m {valores[c]}\033[m ', end='')
    print('PRONTO!')


def somaPar(lst):
    epar = 0
    print(f'Somando os valores pares de \033[32m{lst}\033[m, temos:', end='')
    for par in lst:
        if par % 2 == 0:
            epar += par
    sleep(1)
    print(f' \033[1;31m{epar}\033[m')


sorteia()
somaPar(valores)