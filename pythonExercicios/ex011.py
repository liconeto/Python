texto = ' Desafio 011 '
print(' {:*^30}'. format(texto))
nl = float(input('Digite a medida da largura: '))
na = float(input('Digite a medida da altura: '))
print(' A Largura informada foi : {}.\n A altura informada foi : {}.\n A área do local é: {:.2f}.\n'
      ' A quantidade de tinta para pintar a área calculada : {:.2f}' .format(nl, na, nl * na, (nl * na)/2))