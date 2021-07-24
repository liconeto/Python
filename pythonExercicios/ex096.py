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

texto2 =' \033[32m Função adaptativa \033[m '
print(f'{texto2:*^50}')

def area(largura, comprimento):
    CalcA = largura * comprimento
    print(f'A área de um terreno de {largura} por {comprimento} é: {CalcA}m²')


print('COntrole de Terreno ')
print('-' * 30)
largura = float(input('LARGURA em (m)'))
comprimento = float(input('COMPRIMENTO em (m)'))
area(largura, comprimento)