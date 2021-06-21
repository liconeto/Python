from datetime import date
from emoji import emojize
from time import sleep
from random import randint

<<<<<<< HEAD
texto = ' \033[1;31mDesafio 060\033[m '
=======
texto = ' \033[1;37mDesafio 060\033[m '
>>>>>>> d799d609d2a54bc304b4530f308179459bbea49c
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}
<<<<<<< HEAD
fat = 0

while fat != 1:
    n = int(input('Digite o número para fatorial :'))
    
    print('Fatorial')
=======

texto2 = ' Desafio Fatorial '
print('{:¨^50}'.format(texto2))
n = int(input(' Digite um número :'))
c = f = n
fat = 0
while c != 1:
    f = (f * (c-1))
    fat = f
    c -= 1

print('O Fatorial de \033[31m {}!\033[m é \033[34m{}\033[m'.format(n, fat))
>>>>>>> d799d609d2a54bc304b4530f308179459bbea49c
