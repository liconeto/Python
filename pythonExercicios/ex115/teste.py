from builtins import print

texto = ' \033[1;34m Desafio 115 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[36m Python Módulos \033[m '
print(f'{texto2:*^50}')
from menu import menu

escolha = menu()
print(f'Opção : {escolha}')
