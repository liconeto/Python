from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint
from operator import itemgetter

texto = ' \033[1;36m Desafio 113 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[35m Função LeiInt LeiaFloat \033[m '
print(f'{texto2:*^50}')

def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except(ValueError, TypeError):
            print('\033[1;31mValor Inválido, digite um número inteiro!\033[m')
        except KeyboardInterrupt:
            print('\033[31m O usuário preferiu não informar esses dados!')
            return 0
        else:
            break
    print(f'Você digitou o número inteiro \033[34m{inteiro}\033[m')


def leiaInt2(msg):
    ok = False
    valor = 0
    while True:
        n= str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok = True
        else:
            print('\033[1;31mValor Inválido, digite um número inteiro!\033[m')
        if ok:
            break
    return valor


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except Exception as erro:
            print(f'\033[31mvalor inválido, Digite um valor real!\033[m \033[1;33mO problema foi : {erro}\033[m')
        else:
            break
    return n

n = leiaInt('Digite um valor: ')
n = leiaInt2('Digite um valor: ')
print(f'Valor de N {n}')
n= leiaFloat('Digite um valor real!')