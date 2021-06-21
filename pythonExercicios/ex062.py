from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;37mDesafio 062\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

t = int(input('Digite o termo da PA :'))
r = int(input('Digite a razão da PA :'))
l = int(input('Digite quantos termos :'))
cont = l
while l != 0:
    print(t, end='\033[33m -> \033[m')
    sleep(0.3)
    t += r
    l -= 1
    if l == 0:
        l= int(input('\033[35m Quer mostrar mais quantos termos ?:\033[m'))
        cont += l
print('\033[36mTermos calculados: {}\033[m' .format(cont))
print('\033[31mFIM! {}\033[m' .format(emojize(':zap:', use_aliases=True)))
