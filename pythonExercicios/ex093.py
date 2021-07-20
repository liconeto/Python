from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint
from operator import itemgetter

texto = ' \033[1;31m Desafio 093 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[32m Aproveitamento Jogador \033[m '
print(f'{texto2:*^50}')
partidas = total =0
jogador = dict()
gols= list()
nome = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {nome} jogou? '))
for i in range(1, partidas+1):
    gols.append(int(input(f'  * Quantos gols na partida {i}: ')))
for i, c in enumerate(gols):
    total += c
print('+*' * 30)
jogador= {'nome': nome, 'gols': gols[:], 'total': total}
print(f'{jogador}')
print('*+' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('+*' * 30)
print(f' O Jogador {jogador["nome"]} jogou {partidas} partidas.')
for k, v in jogador.items():
    if k == 'gols':
        for i, c in enumerate(v):
            sleep(0.5)
            print(f'   => Na patida \033[32m{i+1}\033[m, fez \033[31m{c}\033[m gols')
print(f' Um total de \033[31m{jogador["total"]}\033[m gols')
print('+*' * 30)