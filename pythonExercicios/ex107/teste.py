from builtins import print

texto = ' \033[1;35m Desafio 107 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[32m Python Módulos \033[m '
print(f'{texto2:*^50}')

import moeda

num = float(input('Digite um valor: R$'))
aumentar = moeda.aumentar(num, 10)
diminuir = moeda.diminuir(num, 13)
metade = moeda.metade(num)
dobro = moeda.dobro(num)
print(f'A metade de {num} é R${metade}')
print(f'O dobro de {num} é R${dobro}')
print(f'O valor {num} maior em 10% é R${aumentar}')
print(f'O valor {num} menor em 13% é R${diminuir}')

