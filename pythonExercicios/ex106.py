from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint
from operator import itemgetter

texto = ' \033[1;31m Desafio 106 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[32m Função Mini Help Python \033[m '
print(f'{texto2:*^50}')

def ajuda(funcao=False):
    """
    -> função para interação e ajuda da funções internas do Python
    :param funcao: nome da função ou biblioteca
    :return: as informações de ajuda da função escolhida com base nas informações do Python help()
    """
    while True:
        print('\033[42m~\033[m' * 60)
        textof='Sistema de ajuda PyHelp'
        print(f'\033[42m{textof:^60}\033[m')
        print('\033[42m~\033[m' * 60)
        funcao = str(input('Função ou Biblioteca > '))
        if funcao == 'FIM':
            print('\033[41m¨' * 40)
            fim = 'ATÉ LOGO !'
            print(f'{fim:^40}')
            print('¨' * 40)
            break
        sleep(0.5)
        print('\033[44m~\033[m' * 60)
        textof2 = 'Acessando o manual do comando '+funcao
        print(f'\033[44m{textof2:^60}\033[m')
        print('\033[44m~\033[m' * 60)
        sleep(1)
        print('\033[7m')
        if funcao:
            help(funcao)

ajuda()