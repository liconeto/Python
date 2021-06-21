from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;31mDesafio 060\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}
fat = 0

while fat != 1:
    n = int(input('Digite o número para fatorial :'))
    
    print('Fatorial')