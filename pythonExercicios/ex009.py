texto = ' Desafio 009 '
print(' {:*^30}'. format(texto))
n = int(input('Digite um valor: '))
print(' O valor digitado foi : {}.\n E sua tabuada é:\n | {} x 0 = {} |\n | {} x 1 = {} | \n | {} x 2 = {} | \n | {} x 3 = {} | \n'
      ' | {} x 4 = {} | \n | {} x 5 = {} | \n | {} x 6 = {} | \n | {} x 7 = {} | \n | {} x 8 = {} | \n | {} x 9 = {} | \n | {} x 10 = {} | \n'
      .format(n, n, n * 0, n, n * 1, n, n * 2, n, n * 3, n, n * 4, n, n * 5, n, n * 6, n, n * 7, n, n * 8, n, n * 9, n, n * 10))
texto2 = ' Desafio 009 com For '
print(' {:*^30}'. format(texto2))
print(' O valor digitado foi : {}' .format(n))
for i in range(11): print('| {} x {} = {} |' .format(n, i, n * i))
