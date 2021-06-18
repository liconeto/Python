from emoji import emojize
from time import sleep
from datetime import date

texto = ' \033[1;31mDesafio 057\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o sexo \033[1;35m[ M | F ] \033[m:')).upper()

if sexo == 'M':
    print('Seu sexo é ={}Masculino' .format(cores['azul']))
else:
    print('Seu sexo é {}Feminino' .format(cores['vermelho']))
print('FIM !')