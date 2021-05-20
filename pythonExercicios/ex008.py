texto = ' Desafio 008 '
print(' {:*^30}'. format(texto))
n1 = float(input('Digite o valor em metros : '))
print(' O valor digitado em metros foi : {} \n '
      'Em quilômetros : {} \n Em hectômetro : {} \n Em decâmetro : {}\n '
      'Em centimetros : {} \n Em milimetros : {}'
      .format(n1, n1 / 1000, n1 / 100, n1 / 10, n1 * 100, n1 * 1000))