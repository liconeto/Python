from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint
from operator import itemgetter

texto = ' \033[1;34m Desafio 098 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[33m Função Contador \033[m '
print(f'{texto2:*^50}')

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print('-=' * 30)
    print(f'A contagem de {inicio} até {fim} de {passo} em {passo}: ')

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.4)
            cont += passo
        print(' FIM!')
        print('-=' * 30)
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.4)
            cont -= passo
        print(' FIM!')
        print('-=' * 30)



contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 30)
print('É hora de fazer uma contagem personalizada!')
inicio = int(input('Informe o valor de inicio: '))
fim = int(input('Informe o final: '))
passo = int(input('Informeo passo: '))
contador(inicio, fim, passo)