from emoji import emojize
from time import sleep
from datetime import date

texto = ' \033[1;31mDesafio 057\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}
'''
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o sexo \033[1;35m[ M | F ] \033[m:')).upper()

if sexo == 'M':
    print('Seu sexo é ={}Masculino' .format(cores['azul']))
else:
    print('Seu sexo é {}Feminino' .format(cores['vermelho']))
print('FIM !')
'''
sexo = str(input('Digite seu sexo [ M | F ]:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo Invalído! Por favor informe o sexo [ M | F ]:'))
if sexo == 'F' or sexo =='f':
    print('Sexo \033[31mFeminino \033[m')
else:
    print('Sexo \033[34mMasculino \033[m')
print('Sexo {} registrado com sucesso' .format(sexo))