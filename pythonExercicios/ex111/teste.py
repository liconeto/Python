from builtins import print

texto = ' \033[1;36m Desafio 111 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[31m Python Módulos \033[m '
print(f'{texto2:*^50}')
from ex111.utilidadesCeV import moeda
while True:
    try:
        num = float(input('Digite um valor: R$ '))
    except:
        print('Valor inválido informe um valor')
    else:
        break
while True:
    try:
        pctS = int(input('Porcentagem de aumento: '))
    except:
        print('Valor inválido, digite um número inteiro!')
    else:
        break
while True:
    try:
        pctD = int(input('Porcentagem de redução: '))
    except:
        print('Valor inválido, digite um número inteiro!')
    else:
        break
moeda.resumo(num, pctS, pctD)



