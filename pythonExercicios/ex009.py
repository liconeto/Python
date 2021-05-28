texto = ' Desafio 009 '
print('\033[1;34m {:*^30}\033[m'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}
n = int(input('Digite um valor: '))
print('{} O valor digitado foi : {}.\n E sua tabuada é:\n | {} x 0 = {:2} |\n | {} x 1 = {:2} | \n | {} x 2 = {:2} | \n | {} x 3 = {:2} | \n'
      ' | {} x 4 = {:2} | \n | {} x 5 = {:2} | \n | {} x 6 = {:2} | \n | {} x 7 = {:2} | \n | {} x 8 = {:2} | \n | {} x 9 = {:2} | \n | {} x 10 = {} | {}\n'
      .format(cores['ciano'],n, n, n * 0, n, n * 1, n, n * 2, n, n * 3, n, n * 4, n, n * 5, n, n * 6, n, n * 7, n, n * 8, n, n * 9, n, n * 10, limpa))
texto2 = ' Desafio 009 com For '
print('{} {:*^30}{}'. format(cores['verde'], texto2, limpa))
print(' O valor digitado foi : {}' .format(n))
for i in range(11): print('{}| {} x {:2} = {:2} |{}' .format(cores['azul'],n, i, n * i, limpa))
