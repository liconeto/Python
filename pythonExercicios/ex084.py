from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;35m Desafio 084 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[34m Lista composta \033[m'
print(f'{texto2:*^50}')

pessoas = list()
pessoa = list()
pesada = list()
leve = []
while True:
    pessoa.append(str(input('Digite o nome :')))
    pessoa.append(int(input('Digite o peso :')))
    pessoas.append(pessoa[:])
    pessoa.clear()
    continua = str(input('Deseja continuar? [S/N]')).strip()[0]
    if continua in 'nN':
        break
print(f'{pessoas}')
print(f'A lista tem \033[31m{len(pessoas)}\033[m pessoas cadastradas.')
print(f'{"-=" * 30}')
for p in pessoas:
    print(p)
    if p[1] >= 100:
        pesada.append(p[:])
    elif p[1] <= 70:
        leve.append(p[:])
print(f'-=' * 30)
print(f'As pessoas mais pesadas são')
print(f'{pesada}')
print(f'-=' * 30)
print(f'As pessoas mais leves são')
print(f'{leve}')