from builtins import print

texto = ' \033[1;36m Desafio 109 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[34m Python Módulos \033[m '
print(f'{texto2:*^50}')
from ex109 import moeda

num = float(input('Digite um valor: R$ '))
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'O valor {moeda.moeda(num)} maior em 10% é {moeda.aumentar(num, 10, True)}')
print(f'O valor {moeda.moeda(num)} menor em 13% é {moeda.diminuir(num, 13, True)}')


