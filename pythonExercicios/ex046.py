from time import sleep
from emoji import emojize

texto = ' Desafio 046 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

print('{}Contador Curso em Vídeo' .format(cores['ciano']))

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emojize(" {}:fireworks::fireworks::fireworks::fireworks::fireworks:", use_aliases=True) .format(cores['vermelho']))