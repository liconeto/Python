from builtins import print

texto = ' \033[1;36m Desafio 108 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[32m Python Módulos \033[m '
print(f'{texto2:*^50}')
from ex108 import moeda

num = float(input('Digite um valor: R$'))
aumentar = moeda.aumentar(num, 10)
diminuir = moeda.diminuir(num, 13)
metade = moeda.metade(num)
dobro = moeda.dobro(num)
print(f'A metade de {moeda.moeda(num)} é R${moeda.moeda(metade)}')
print(f'O dobro de {moeda.moeda(num)} é R${moeda.moeda(dobro)}')
print(f'O valor {moeda.moeda(num)} maior em 10% é R${moeda.moeda(aumentar)}')
print(f'O valor {moeda.moeda(num)} menor em 13% é R${moeda.moeda(diminuir)}')

