from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;35mDesafio 074\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[37m Tupla Aleatória \033[m '
print(f'{texto2:*^50}')
numeros = (randint(0, 999), randint(0, 999), randint(0, 999),
         randint(0, 999), randint(0, 999) )

separador =''
print('Os números gerados aleatóriamente foram.')
print(f'{numeros}')
print(f'\033[33m{separador:#^50}\033[m')
print('\033[35m     Ordenando o números! ', end='')
for c in range(0,5):
    print('\033[35m.\033[m', end='')
    sleep(0.6)
print('')
ordenada = sorted(numeros)
print(f'{ordenada}')
print(f'\033[34m{separador:#^50}\033[m')

print(f''' O menor número é {ordenada[0]}.
 E o maior número é {ordenada[-1]}.''')