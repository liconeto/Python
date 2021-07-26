from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint
from operator import itemgetter

texto = ' \033[1;36m Desafio 104 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[34m Função Ficha Jogador \033[m '
print(f'{texto2:*^50}')

def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except:
            print('\033[1;31mValor Inválido, digite um número inteiro!\033[m')
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



n = leiaInt('Digite um valor: ')
n = leiaInt2('Digite um valor: ')
print(f'Valor de N {n}')