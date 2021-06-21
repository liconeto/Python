from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;36mDesafio 064\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}
texto2 = ' \033[1;35mDesafio Conta e Soma\033[m '
print('{:#^50}' .format(texto2))

n = 0
c = 0
s = 0

while n != 999:
    n = int(input('\033[31m Digite um número inteiro :\033[m'))
    if n != 999:
        c += 1
        s = s + n
print('Contador : \033[33m{}\033[m' .format(c))
print('Soma : \033[34m{}\033[m' .format(s))
