import urllib.error
from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint
from operator import itemgetter
from urllib import request

texto = ' \033[1;36m Desafio 114 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[34m Função testa link \033[m '
print(f'{texto2:*^50}')

try:
    pudim = request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessivel no momento!')
else:
    print('Consegui acessar o site Pudim com sucesso!')
print(f'{pudim.read()}')
