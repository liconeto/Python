from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;31m Desafio 090 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[36m Situação Aluno \033[m '
print(f'{texto2:*^50}')

aluno = dict()

while True:
    try:
        nome = str(input('Nome do Aluno: '))
    except:
        print('Informe o nome do aluno! ')
    else:
        break
while True:
    try:
        media = float(input('digite a média :'))
    except:
        print('Valor inválido, digite a média do aluno: ')
    else:
        break
print('=-' * 30)
aluno['nome'] = nome
aluno['media'] = media
if media >= 7:
    aluno['situacao'] = '\033[34mAPROVADO\033[m'
elif media < 7 and media >= 5:
    aluno['situacao'] = '\033[37mRECUPERAÇÂO\033[m'
else:
    aluno['situacao'] = '\033[31mREPROVADO\033[m'
print(f'{aluno}')
print('*+' * 35)
print(f'| Nome:\033[32m{aluno["nome"]:<20}\033[m, média é {aluno["media"]} Situação: {aluno["situacao"]:^14} |')
print('+*' * 35)