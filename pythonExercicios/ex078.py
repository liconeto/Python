from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;34m Desafio 078 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[33m Lista de Valores \033[m '
print(f'{texto2:*^50}')

valores = []

pmenor = []
pmaior = []
for cont in range(0, 5):
    while True:
        try:
            valores.append(int(input('Digite um valor: ')))
        except:
            print('Valor inválido, digite um número inteiro!')
        else:
            break

print(f'Os valores digitados foram {valores}')

for p, v in enumerate(valores):
    if p == 0:
        maior = v
        menor = v

    if menor >= v:
        menor = v

    if maior <= v:
        maior = v


for p, v in enumerate(valores):
    if menor == v:
        pmenor.append(p+1)
    if maior == v:
        pmaior.append(p+1)
print(f'O menor valor é \033[32m{menor}\033[m nas posições \033[34m{pmenor}\033[m')
print(f'O maior valor é \033[31m{maior}\033[m nas posições \033[34m{pmaior}\033[m')