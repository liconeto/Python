from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;37m Desafio 088 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[36m Palpite Mega Sena\033[m '
print(f'{texto2:*^50}')

lista = list()
jogos = list()
qtde = 0
while True:
    try:
        qtde = int(input('Quantos jogos você deseja que eu sorteie? : '))
    except:
        print('Valor inválido, digite um valor inteiro!')
    else:
        break
print('\033[31m*-\033[m' * 30)
while qtde != 0:
    for c in range(1, 7):
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
    qtde -= 1
    jogos.append(sorted(lista[:]))
    lista.clear()
print(f'Sorteando jogos!')
for c in jogos:
    sleep(1)
    print(c)
print('\033[31m-*\033[m' * 30)
sleep(1)
print(f'\033[32m        *** BOA SORTE! ***')