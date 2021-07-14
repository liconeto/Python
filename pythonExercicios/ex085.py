from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;32m Desafio 085 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[34m Lista composta  par e impar \033[m'
print(f'{texto2:*^50}')

numeros = [[],[]]

for v in range(1, 8):
    while True:
        try:
            num = int(input(f'Digite o {v}º valor :'))
        except:
            print('Valor inválido, Digite um número inteiro!')
        else:
            break
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print(numeros)
print(f'Os valores pares são: {sorted(numeros[0])}')
print(f'Os valores impares são: {sorted(numeros[1])}')
