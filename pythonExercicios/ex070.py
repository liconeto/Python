import random
from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;34mDesafio 070\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[35m Lojas CEV\033[m '
print(f'{texto2:*^50}')

totalCompra = 0
maisMil = 0
maisBarato = 0
nmaisBarato = ''

while True:
    nomep = str(input('Qual o produto? :'))

    while True:
        try:
            preco = float(input('Qual o valor R$: '))
        except:
            print('Valor inválido, Digite o Preço do produto!')
        else:
            break

    if totalCompra == 0:
        nmaisBarato = nomep
        maisBarato = preco
    elif maisBarato > preco:
        maisBarato = preco
        nmaisBarato = nomep

    if preco > 1000:
        maisMil += 1

    totalCompra += preco

    continua = str(input('Deseja comprar algo mais? : [ S | N ]')).strip()[0]
    while continua not in ['s', 'S', 'n', 'N']:
        continua = str(input('Deseja comprar algo mais? : [ S | N ]')).strip()[0]
    if continua == 'n' or continua == 'N':
        break
print(f'''
| O total da compra foi \033[1;31m{totalCompra:.2f}\033[m |
| Produtos acimas de mil reais foram \033[32m{maisMil}\033[m |
| O produto mais barato é \033[34m{nmaisBarato}\033[m e custa \033[32m{maisBarato}\033[m |''')
print('Fim!')