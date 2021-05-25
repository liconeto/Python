texto = ' Desafio 027 '
print(' {:*^30}'. format(texto))
nome = str(input('Digite seu nome completo : ')).strip()
nome = nome.split()
print('O nome digitado foi : {}' .format(nome))
print('Primeiro nome : {} \n'
      'Ultimo nome : {} ' .format(nome[0], nome[len(nome) - 1 ]))