from emoji import emojize

texto = ' Desafio 047 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

print('{}Contador par Curso em Vídeo {}{}' .format(cores['roxo'], emojize(":warning:"), limpa))

for c in range(2, 51, 2):
    print(c, end=' ')

for c in range (0, 51):
    if c % 2 == 0:
        print(', {}{:2}{}' .format(cores['azul'], c, limpa ))