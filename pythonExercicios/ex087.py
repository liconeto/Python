from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;31m Desafio 087 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[34m Matriz 3x3 aprimorada\033[m'
print(f'{texto2:*^50}')
'''
matriz = [[], [], []]
pares = col3 = 0

for c in range(1, 10):
    while True:
        try:
            num = int(input(f'Digite o valor {c} : '))
        except:
            print('Valor inválido, Digite um valor inteiro!')
        else:
            break
    if c <= 3:
        matriz[0].append(num)
    elif c > 3 and c <= 6:
        matriz[1].append(num)
    else:
        matriz[2].append(num)
for i, v in enumerate(matriz):
    print(f'\033[1;35m{v}\033[m')
    col3 += matriz[i][2]
    for c in v:
        if c % 2 == 0:
            pares += c
for i,c in enumerate(matriz[1]):
    if i == 0:
        maior = c
    if maior < c:
        maior = c
print()
print(f'A soma dos valores par é : \033[34m{pares}\033[m')
print(f'A soma dos valores da 3ª coluna : \033[1;33m{col3}\033[m')
print(f'A segunda linha tem o valores \033[1;32m{matriz[1]}\033[m é : \033[31m{maior}\033[m')
'''
matriz2 = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
smatriz2 = scol3 = smai= 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz2[l][c] = int(input(f'Digite um valor:[{l},{c}] '))
print('-+' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz2[l][c]:^5}]', end='')
        if matriz2[l][c] % 2 == 0:
            smatriz2 += matriz2[l][c]


    scol3 += matriz2[l][2]
for c in range(0,3):
    if c == 0:
        smai = matriz2[1][c]
    elif matriz2[1][c] > smai:
        smai = matriz2[1][c]


    print()
print(f'A soma da Matriz é: \033[1;34m{smatriz2}\033[m')
print(f'A dos Valores da 3 coluna \033[32m {scol3}\033[m')
print(f'O maior valor da segunda linha 2 : {smai}')