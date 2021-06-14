from emoji import emojize
from time import sleep

texto = ' Desafio 049 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}
print("{}{}Tabuada Curso em Vídeo{}" .format(cores['ciano'], emojize(":star::star::star::star::star:"), limpa))

num = int(input('{}Informe o número para gerar a tabuada :{}' .format(cores['amarelo'], limpa)))
print('O número escolhido foi {}' .format(num))
for c in range(1,11):
    sleep(0.2)
    print('|  {}{:2}{} X {}{:2}{}= {}{:2}{} |' . format(cores['verde'], c, limpa, cores['azul'], num, limpa, cores['vermelho'], c * num, limpa))