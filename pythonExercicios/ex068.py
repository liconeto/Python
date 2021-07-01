import random
from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;36mDesafio 068\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[34m Par\033[m ou \033[32mImpar\033[m '
print(f'{texto2:*^50}')

v=0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um número inteiro : '))
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Escolha Par ou Impar = [ P | I ] :')).strip()[0].upper()
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou')
            v+=1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!')
            v+=1
        else:
            print('Você perdeu!')
            break
    print(f'Computador :{computador} e jogador {jogador} = {total} ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
print(f'Vitórias sonsecutivas : {v}')
