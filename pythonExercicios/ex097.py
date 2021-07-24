from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint
from operator import itemgetter

texto = ' \033[1;34m Desafio 097 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[35m Função texto \033[m '
print(f'{texto2:*^50}')

def escreva(txt):
    tamanho = len(txt) + 4
    print('~' * tamanho)
    print(f'{txt:^{tamanho}}')
    print('~' * tamanho)
    print('')


escreva('Gustavo')
escreva('Cev')
escreva('Olho no céu!')