from emoji import emojize
from time import sleep

texto = ' Desafio 050 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

print('{}Soma pares Curso em vídeo{}' .format(cores['vermelho'], limpa))
soma = 0
for c in range(1, 7):
    n = int(input('Valor :'))
    if n % 2 == 0:
        soma = soma + n
print('Soma :{}' .format(soma))