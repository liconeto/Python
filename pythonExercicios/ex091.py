from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;36m Desafio 091 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[34m Jogadores \033[m '
print(f'{texto2:*^50}')
jogador= dict()
jogadores = dict()

for k in range(1, 5):
    jogador['jogador'] = k
    v = randint(1, 6)
    jogador['dado'] = v
    print(jogador)
    jogadores['jogador'] =jogador.copy()
print(f'{jogadores.items()}')