from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;37mDesafio 063\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

print('Desafio Fibonacci')
n = int(input('Digite o numero inteiro :'))
e = int(input('Quantos elementos quer ver ? :'))
fb=0
while e != 0:
    fb = (n-1)+()
    e-= 1