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
tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
      'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
      'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
n=0
while True:
    try:
        n = int(input('Digite um número entre 0 e 20  :'))
    except:
        print('Valor inválido, digite um número entre 0 e 20 :')

    if 0 <= n and n <= 20:
        print(f'{tupla[n]}')
