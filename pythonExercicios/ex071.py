import random
from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;37mDesafio 071\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[35m Caixa Eletrônico CEV\033[m '
print(f'{texto2:*^50}')

conta50 = conta20 = conta10 = conta1 = 0

print('.: \033[1;32mBem-vindo ao Caixa Eletrônico do CEV!\033[m :.')
while True:
    try:
        valor = int(input('Digite o valor do saque:'))
    except:
        print('valor inválido, Digite um número inteiro!')
    else:
        break

conta50 = valor / 50

if (valor % 50) > 20:
    conta20 = (valor % 50) / 20
if (valor % 20) > 10:
    conta10 = (valor % 20) / 10
if (valor % 10) >= 1:
    conta1 = (valor % 10) / 1

print(f'O valor do saque :{valor}')
print('Calculando quantidade de notas ', end='')
for c in range(5):
    print('\033[31m.\033[m', end='')
    sleep(0.4)
print('')
print(f'notas de 50 : \033[31m{int(conta50)}\033[m')
print(f'notas de 20 : \033[34m{int(conta20)}\033[m')
print(f'notas de 10 : \033[35m{int(conta10)}\033[m')
print(f'notas de  1 : \033[36m{int(conta1)}\033[m')