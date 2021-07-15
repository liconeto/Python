from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;36m Desafio 086 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[35m Matriz 3x3 \033[m'
print(f'{texto2:*^50}')

matriz =[[],[],[]]

for c in range(1, 10):
    while True:
        try:
            num = int(input(f'Digite o valor {c} :'))
        except:
            print('Valor Inválido, Digite um valor inteiro!')
        else:
            break
    if c <= 3:
        matriz[0].append(num)
    elif c > 3 and c <= 6:
        matriz[1].append(num)
    else:
        matriz[2].append(num)

print(matriz)
for i in matriz:
    print(f'\033[1;31m{i}\033[m')