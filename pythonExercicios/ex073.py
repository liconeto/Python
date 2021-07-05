import random
from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;34mDesafio 072\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[35m Tupla extenso \033[m '
print(f'{texto2:*^50}')

tupla = ('Bragantino', 'Athletico-PR', 'Palmeiras', 'Atlético-MG', 'Fortaleza',
         'Bahia', 'Atlético-GO', 'Ceará', 'Fluminense', 'Flamengo', 'Santos',
         'Juventude', 'Corinthians', 'Internacional', 'América-MG', 'Sport',
         'São Paulo', 'Cuiabá', 'Chapecoense', 'Grêmio')
separador ='='
print('\033[32mOs 5º colocados são:\033[m')
for time in range(0,5):
    print(f'{time+1}º {tupla[time]}')

print(f'\033[33m{separador:=^50}\033[m')

print('\033[31m Os 4 ultimos colocados são:\033[m')
for time in range(16, 20):
    print(f'{time+1}º {tupla[time]}')

print(f'\033[36m{separador:=^50}\033[m')

ordenada = sorted(tupla)
for pos, time in enumerate(ordenada):
    print(f'{pos+1}:{time}')

print(f'\033[37m{separador:=^50}\033[m')

print(f'A Chapecoense está na posição :{tupla.index("Chapecoense")+1}')