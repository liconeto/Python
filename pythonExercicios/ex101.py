from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint
from operator import itemgetter

texto = ' \033[1;33m Desafio 101 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[35m Função VOTO! \033[m '
print(f'{texto2:*^50}')
nasc = 0
def voto(anoN):
    ano = date.year
    idade = ano - anoN
    if 16 < idade:
        rVoto = 'NEGADO'
    elif 16 > idade < 18 or idade > 65:
        rVoto = 'OPICIONAL'
    elif 18 > idade < 65:
        rVoto = 'OBRIGATORIO'

    return rVoto



nasc = int(input('Digite seu ano de nascimento: '))
msg = voto(nasc)
print(f'{msg}')