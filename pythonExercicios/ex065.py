from builtins import input, print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;36mDesafio 065\033[m '
print('{:*^50}'. format(texto))
continua ='S'
cont =0
maior = menor = 0
soma =0
while continua not in 'nN':
    n = int(input('Digite um número :'))
    cont += 1
    soma += n
    media = soma / cont
    if cont == 1:
        maior =n
        menor =n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    continua = str(input('Você deseja continuar? [S|N]:')).upper().strip()[0]

print('''
|  Quantidade :\033[35m{}\033[m  |
|  A média : \033[36m{:.2f}\033[m  |
|  O maior : \033[31m{}\033[m  |
|  O Menor : \033[34m{}\033[m  |''' .format(cont, media, maior, menor))
print('\033[35mAcabou!')