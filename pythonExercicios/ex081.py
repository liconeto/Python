from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \034[1;33m Desafio 081 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[36m Lista Ordenados Decrescente \033[m '
print(f'{texto2:*^50}')

lista =[]
cinco = []
continua ='S'
while continua == 'S':
    while True:
        try:
            valor = int(input('Digite um valor inteiro :'))
        except:
            print('Valor invalido, digite um valor inteiro')
        else:
            break
    lista.append(valor)

    continua = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
for p, v in enumerate(lista):
    if 5 == lista[p]:
        cinco.append(p)
print(f'A lista tem \033[31m{len(lista)}\033[m itens')
print(f'Os números digitados foram = \033[34m{sorted(lista, reverse=True)}\033[m')
print(f'O número cinco foi digitado {len(cinco)} vezes na posições {cinco}')