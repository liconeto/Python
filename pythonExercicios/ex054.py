from emoji import emojize
from time import sleep
from datetime import date

texto = ' Desafio 054 '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' Verificador de maioridade Curso em vìdeo '
print('{}{:#^50}{}' .format(cores['roxo'], texto2, limpa))

ano = date.today().year
maior =0
menor =0

for c in range(1, 8):
    idade = int(input('Informe o {}º ano da nascimento para verificação :' .format(c)))
    if (ano - idade )>= 21:
        maior = maior + 1
        #print((ano - idade ))
    else:
        menor = menor + 1
        #print(ano - idade)
print('Calculando')
sleep(1)
print('''
Os maiores de 21 são : {}{}{}
e os menores são : {}{}{}''' .format(cores['azul'], maior, limpa, cores['vermelho'], menor, limpa))