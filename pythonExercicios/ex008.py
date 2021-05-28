texto = ' Desafio 008 '
print('\033[1;34m {:*^30}\033[m'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}
n1 = float(input('{}Digite o valor em metros : {}'. format(cores['vermelho'], limpa)))
print(' O valor digitado em metros foi : {} \n '
      'Em quilômetros : {} \n Em hectômetro : {} \n Em decâmetro : {}\n '
      'Em centimetros : {} \n Em milimetros : {}'
      .format(n1, n1 / 1000, n1 / 100, n1 / 10, n1 * 100, n1 * 1000))