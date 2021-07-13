from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \034[1;34m Desafio 082 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[32m Lista Ordenados lista para e impar \033[m '
print(f'{texto2:*^50}')

lista = []
par = []
impar = []
continua = 'S'
while continua != 'N':
    while True:
        try:
            valor = int(input('Digite um número inteiro :'))
        except:
            print('Valor inválido, Digite um número inteiro !')
        else:
            break
    lista.append(valor)
    if valor % 2 == 0:
        print('Número par adicionado!')
        par.append(valor)
    else:
        print('Número impar adicionado!')
        impar.append(valor)
    continua = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

print(f'Os valores digitados foram \033[1;33m{sorted(lista)}\033[m')
print(f'Os números pares são : \033[34m{sorted(par)}\033[m')
print(f'Os números impares são : \033[31m{sorted(impar)}\033[m')
