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

texto2 =' \033[32m Validardor de expressões \033[m '
print(f'{texto2:*^50}')

expressao = []
