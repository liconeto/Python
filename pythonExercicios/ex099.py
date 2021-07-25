from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint
from operator import itemgetter

texto = ' \033[1;34m Desafio 099 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[33m Função Maior \033[m '
print(f'{texto2:*^50}')


def maior( * num ):
    contador = 0
    vmaior = 0
    print('-*' * 30)
    print('Analisando valores passados!...')
    for i, c in enumerate(num):
        print(f' \033[33m{c}\033[m ', end='')
        sleep(0.4)
        contador += 1
        if i == 0:
            vmaior = c
        elif c > vmaior:
            vmaior = c
    print(f'| Foram informados {contador} valores ao todo |')
    sleep(0.5)
    print(f'| O maior valor informado foi: \033[35m{vmaior}\033[m |')
    print('*-' * 30)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()