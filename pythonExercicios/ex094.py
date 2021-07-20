from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint
from operator import itemgetter

texto = ' \033[1;35m Desafio 094 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[34m Pessoas \033[m '

pessoas = list()
pessoa = {}
sexo = ' '
while True:
    while True:
        try:
            nome = str(input('Nome :'))
        except:
            print('Informe o nome!')
        else:
            break
    while True:
        try:
            sexo = str(input('Informe o sexo [M/F]: ')).strip()[0]
        except:
            print('informe o sexo [M/F')
        else:
            break
    while True:
        try:
            idade= int(input(f'Infome sua idade {nome} : '))
        except:
            print('Valor inválido, informe a idade!')
        else:
            break
    pessoa = {'nome': nome, 'sexo': sexo, 'idade': idade}
    pessoas.append(pessoa.copy())
    continua = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continua in 'nN':
        break
print(f'{pessoa}')
print(f'{pessoas}')