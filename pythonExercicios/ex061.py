from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;37mDesafio 061\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

t = int(input('Digite o termo da PA :'))
r = int(input('Digite a razão da PA :'))
l = 10
while l != 0:
    print(t, end='\033[33m -> \033[m')
    t += r
    l -= 1
print('\033[31mFIM!')
