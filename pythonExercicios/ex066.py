from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;37mDesafio 066\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[32mUsando Break\033[m'
print(f'{texto2:*^50}')
c = s = 0
while True:
    while True:
        try:
            n = int(input('Digite um número inteiro : [\033[31m999\033[m para parar]'))
        except ValueError as e:
            print(f'Valor inválido, digite um número inteiro!')
        else:
            break
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou \033[34m{c} \033[me a soma entre eles é : \033[31m{s}\033[m')