from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint
from operator import itemgetter

texto = ' \033[1;36m Desafio 103 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[34m Função Ficha Jogador \033[m '
print(f'{texto2:*^50}')

def ficha(jogador='Desconhecido', qgols=0):
    jogadorV = jogador
    gols = qgols
    return print(f'|  \033[36m{jogadorV:<30}\033[m, fez \033[31m{gols:5>}\033[m gols.  |')


nome = str(input('Nome do jogador :'))
qgols = str(input('quatidade de gols :'))

if qgols.isnumeric():
    qgols = int(qgols)
else:
    qgols = 0
if nome.strip() == '':
    print('-=' * 25)
    ficha(qgols=qgols)
    print('=-' * 25)
else:
    print('-=' * 25)
    ficha(nome, qgols)
    print('=-' * 25)
