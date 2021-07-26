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
    """
    -> calcula a idade do eleitor e retorna a informação se o voto é NEGADO, OPICIONAL ou OBRIGATORIO
    :param anoN: recebe o ano de nascimento
    :return: retorna uma STRING contendo as seguinte opções (NEGADO, OPICIONAL ou OBRIGATORIO)
    """
    ano = date.today().year
    idade = ano - anoN
    #print(f'Ano do sistema {ano}')
    print(f'Sua idade é : {idade}', end=', seu voto é: ')
    if 16 > idade:
        rVoto = '\033[1;31mNEGADO\033[m'
    elif 16 <= idade < 18 or idade > 65:
        rVoto = '\033[1;34mOPICIONAL\033[m'
    elif 18 <= idade <= 65:
        rVoto = '\033[1;32mOBRIGATORIO\033[m'

    return rVoto


print(f'{help(voto)}')
nasc = int(input('Digite seu ano de nascimento: '))
Rvoto = voto(nasc)
print(f'{Rvoto}')