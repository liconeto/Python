from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;31mDesafio 059\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

n1 = n2 = 0
opcao = 0
while opcao != 5:
    n1 = int(input('Digite o 1º valor :'))
    n2 = int(input('Digite o 2º valor :'))
    opcao = int(input('''
 |   \033[31m[1] Somar \033[m            |
 |   \033[32m[2] Multiplicar \033[m      |
 |   \033[33m[3] Maior \033[m            |
 |   \033[34m[4] Novos números \033[m    |
 |   \033[35m[5] Sair do Programa!\033[m |'''))

    if opcao == 1:
        print('A soma de {} e {} = {}' .format(n1, n2, n1+n2))
    if opcao == 2:
        print('A multiplicação de {} e {} = {}' .format(n1, n2, n1*n2))
    if opcao == 3:
        if n1 == n2:
            print(' Os números são iguais : {} = {}' .format(n1,n2))
        elif n1 >= n2:
            print('O primeiro é maior que o segundo : {} > {}' .format(n1,n2))
        else:
            print('O segundo número é maior que o primeiro : {} < {}' .format(n2,n1))

    if opcao == 4:
        print('')

print('\033[31mFIM !')