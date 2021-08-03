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

texto2 =' \033[34m Função com Validação de dados \033[m '
print(f'{texto2:*^50}')

def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError) as erro:
            print('\033[1;31mValor Inválido, digite um número inteiro!\033[m')
            print(f'\033[1;33mO erro foi: {erro}\033[m')
        except KeyboardInterrupt:
            print('O usuário preferiu não informar esse valor!')
        else:
            break
    return inteiro


def leiaFloat(msg):

    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError) as erro:
            print(f'Valor inválido, Informar um valr real válido!')
            print(f'\033[1;33mO erro foi: {erro}\033[m')
        except KeyboardInterrupt:
            print('O usuário preferiu não informar esse valor!')
        else:
            break
    return valor



n = leiaInt('Digite um valor Inteiro: ')
n2 = leiaFloat('Digite um valor Real: ')
print(f'Valor de Inteiro é : \033[34m{n}\033[m e o valor real é : \033[36m{n2}\033[m ')