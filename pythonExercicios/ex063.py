from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;37mDesafio 063\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}
texto2 = ' \033[1;35mDesafio Fibonacci\033[m '
print('{:#^50}' .format(texto2))
n = int(input('Quantos termos você quer mostrar? :'))
t1=0
t2=1
print('~'*30)
print('{} -> {}' .format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}' .format(t3), end='')
    t1 = t2
    t2 = t3
    cont +=1
print(' -> FIM!')
