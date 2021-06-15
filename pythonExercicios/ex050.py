from emoji import emojize
from time import sleep

texto = ' Desafio 050 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

print('{}Soma pares Curso em vídeo{}' .format(cores['vermelho'], limpa))
cont = 0
soma = 0
for c in range(1, 7):
    n = int(input('Digite o {}º Valor :' . format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont += 1
print('Números pares são {} e sua Soma : {}{}' .format(cont, cores['roxo'],soma))