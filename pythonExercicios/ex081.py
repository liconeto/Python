from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \034[1;33m Desafio 081 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[36m Lista Ordenados Decrescente \033[m '
print(f'{texto2:*^50}')

continua ='S'
while continua == 'S':

    continua = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

