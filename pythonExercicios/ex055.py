from emoji import emojize
from time import sleep
from datetime import date

texto = ' Desafio 055 '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}
texto2 =' Comparador de peso Curso em Vídeo '

print('{}{:¬^}{}' .format(cores['ciano'], texto2, limpa))