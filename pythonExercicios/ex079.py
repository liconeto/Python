from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;37m Desafio 079 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[35m Lista Valores Únicos \033[m '
print(f'{texto2:*^50}')

unicos = []
continua = 'S'
while continua == 'S':
    while True:
        try:
            num = int(input('Digite um número :'))
        except:
            print('Valor inválido, digite um número inteiro!')
        else:
            break
    if num not in unicos:
        unicos.append(num)
    continua = str(input('Deseja continuar ? [S/N] :')).strip().upper()[0]
    while continua not in 'sSnN':
            continua = str(input('Deseja continuar ? [S/N] :')).strip().upper()[0]

print(f'{sorted(unicos)}')