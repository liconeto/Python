from emoji import emojize
from time import sleep

texto = ' Desafio 050 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}
print('{}***{}{} Progressão Aritimética Curso em Vídeo{}{} ***{}' .format(cores['vermelho'], limpa, cores['ciano'], limpa, cores['vermelho'], limpa))
t = int(input('Informe o termo da PA: '))
r = int(input('Informe a razão da PA :'))

for c in range(1, 11):
    print('PA {}' .format(t))
    t = t + r