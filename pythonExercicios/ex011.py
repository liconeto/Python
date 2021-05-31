texto = ' Desafio 011 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}
print('Digite abaixo as informações do local a ser pintado! ')
nl = float(input('Digite a medida da largura: '))
na = float(input('Digite a medida da altura: '))
print(' A Largura informada foi : {}{}{}.\n A altura informada foi : {}{}{}.\n A área do local é: {}{:.2f}{}.\n'
      ' A quantidade de tinta para pintar a área calculada : {}{:.2f}{}' .format(cores['ciano'], nl, limpa, cores['azul'], na, limpa, cores['vermelho'], nl * na, limpa, cores['roxo'], (nl * na)/2, limpa))