from builtins import print

texto = ' \033[1;36m Desafio 109 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[34m Python Módulos \033[m '
print(f'{texto2:*^50}')
from ex110 import moeda

num = float(input('Digite um valor: R$ '))
moeda.resumo(num, 20, 12)



