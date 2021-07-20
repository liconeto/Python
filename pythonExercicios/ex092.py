from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint
from operator import itemgetter

texto = ' \033[1;32m Desafio 092 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[35m Dados Pessoa \033[m '
print(f'{texto2:*^50}')

pessoa = dict()
anoatual = date.today().year

while True:
    try:
        nome = str(input('Informe o nome :'))
    except:
        print('Informe o nome da pessoa!')
    else:
        break
while True:
    try:
        anonasc = int(input('Informe o ano de nascimento: '))
    except:
        print('Valor inválido, informe o ano de nascimento')
    else:
        break
while True:
    try:
        ctps = int(input('Informe o número da CTPS: '))
    except:
        print('Valor inválido, informe o número da CTPS')
    else:
        break
if ctps != 0:
    while True:
        try:
            anocont = int(input('Informe o ano de contratação: '))
        except:
            print('Valor inválido, informar o ano de contratação! ')
        else:
            break
    while True:
        try:
            salario = float(input('Valor do salário: '))
        except:
            print('Valor inválido, informe do valor do salário: ')
        else:
            break
idade = anoatual - anonasc
pessoa = {'nome': nome, 'idade': idade, 'ctps': ctps}
if ctps != 0:
    aposentadoria = idade + ((( anoatual - anocont ) - 35)*-1)

    pessoa ={'nome': nome, 'idade': idade, 'ctps': ctps, 'contratacao':anocont ,'aposentadoria': aposentadoria, 'salario': salario}
print('+*' * 25)
for k, v in pessoa.items():
    print(f'| {k:<20}: {v:<20} | ')
print('*+' * 25)