from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;36m Desafio 075 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[35m Tupla Numérica \033[m '
print(f'{texto2:*^50}')
contNove =0
contPar = 0
valores = (int(input('Digite um número:')), int(input('Digite outro número:')),
           int(input('Digite mais um número:')), int(input('Digite o ultimo número:')))

print(f'{valores}')
for nove in valores:
    if nove == 9:
        contNove += 1

print(f'O número 9 apareceu {contNove} vezes{valores.count(9)}!')
if 3 in valores:
    print(f'O número 3 foi digitado na posição {valores.index(3)+1}')
else:
    print('O número 3 não foi digitado em nenhuma posição!')
print('Números pares:', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')