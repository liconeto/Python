from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;36mDesafio 067\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[32mTabuada Usando Break\033[m'
print(f'{texto2:*^50}')

while True:
    try:
        n = int(input('Digite o número inteiro : '))
    except:
        print('Valor inválido, digite um número inteiro!')
    else:
        c = 0
        if n < 0:
            break
        else:
            while c < 10:
                c += 1
                print(f'''| {n:3} x {c:3} = \033[34m{n*c:4}\033[m |''')
print('Programa tabuada encerrado com sucesso volte sempre ')