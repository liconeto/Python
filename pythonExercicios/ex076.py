from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;32m Desafio 076 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[31m Tupla de preço tabular \033[m '
print(f'{texto2:*^50}')

produtos = ('Caneta', 1.99, 'Celular', 1798.99, 'Monitor', 799.89,
            'Relógio', 499.00, 'Carregador', 45.00, 'Café', 3.50,
            'Notebook', 3569.47, 'Mochila', 179.25)

for c in range(0, len(produtos), 2):
    print(f'| \033[34m{produtos[c] :-<40}R$\033[1;31m{produtos[c+1]:8}\033[m |')
