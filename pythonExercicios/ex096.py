from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint
from operator import itemgetter

texto = ' \033[1;31m Desafio 096 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[32m Função calculo Area \033[m '
print(f'{texto2:*^50}')

def area( largura, comprimento):
    tarea = largura * comprimento
    print(f'A área de um terreno de \033[31m{largura}\033[m x \033[31m{comprimento}\033[m é de : \033[34m{tarea}\033[mm²')


print('CONTROLE DE TERRENO')
print('\033[37m-\033[m'* 30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area(largura, comprimento)
