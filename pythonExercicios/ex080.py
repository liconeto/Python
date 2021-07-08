from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;33m Desafio 080 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[31m Lista Valores Únicos \033[m '
print(f'{texto2:*^50}')

lista = []

for num in range(0, 5):
    while True:
        try:
            valor = int(input('Digite um valor inteiro :'))
        except:
            print('Valor inválido, digite um número inteiro!')
        else:
            break
    if num == 0:
        lista.append(valor)
        print('Primeiro valor da lista!')
        print(f'{lista[num]}')
    if num !=0 and valor > lista[num]:
        lista.insert(2, valor)


print(lista)