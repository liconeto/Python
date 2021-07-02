import random
from builtins import print
from time import sleep

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
        valor = int(input('Digite o valor do saque R$:'))
    except:
        print('valor inválido, Digite um número inteiro!')
    else:
        break
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:


        if totced > 0:
            print(f'Total de \033[1;31m{totced}\033[m cédulas de \033[34m{ced}\033[m')
        if ced == 50:
            ced = 20
            totced = 0
        elif ced == 20:
            ced = 10
            totced = 0
        elif ced == 10:
            ced =1
            totced = 0
        if total == 0:
            break
print(f'O valor do saque :{valor}')

