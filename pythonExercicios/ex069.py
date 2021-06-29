import random
from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;36mDesafio 069\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[34m Cadastro de pessoas\033[m '
print(f'{texto2:*^50}')

maiores = ch = cm =0

while True:
    while True:
        try:
            idade = int(input('Digite a idade :'))
        except:
            print('Valor inválido, digite um número inteiro!')
        else:
            break
    sexo = str(input('Digite o sexo [ \033[31mF\033[m | \033[34mM\033[m ]')).strip()[0]
    while sexo not in ['f', 'F', 'm', 'M']:
            sexo = str(input('Digite o sexo [ \033[31mF\033[m | \033[34mM\033[m ]')).strip()[0]

    if idade >= 18:
        maiores +=1

    if sexo == 'm' or sexo == 'M':
        ch += 1

    if sexo == 'f' and idade < 20 or sexo == 'F' and idade < 20:
        cm += 1

    continua = str(input('Quer continuar ? : [ S | N ]')).strip()[0]
    while continua not in ['n', 'N', 's', 'S']:
        continua = str(input('Quer continuar ? : [ S | N ]')).strip()[0]
    if continua == 'n' or continua == 'N':
        break
print(f'''  .: Foram cadastrados :.
Maiores de idade : \033[32m{maiores}\033[m
Homens : \033[34m{ch}\033[m
Mulheres com menos de 20 : \033[31m{cm}\033[m''')