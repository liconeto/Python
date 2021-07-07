from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;34m Desafio 077 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[36m Tupla de vogais \033[m '
print(f'{texto2:*^50}')

palavras = ('Carro', 'Homologacao', 'Alianca', 'Pedestre', 'Aleluia')

cont =0


while cont != len(palavras):
    vogais =''
    print(f'\nA palavra :\033[33m{palavras[cont]}\033[m tem essas vogais :', end='')
    for letra in palavras[cont]:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    cont += 1