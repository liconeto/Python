texto = ' Desafio 025 '
print(' {:*^30}'. format(texto))
nome = str(input('Digite seu nome completo : '))
nome = nome.split()
print('O nome digitado foi : {} ' .format(nome))

print('Ele tem SILVA ? : {}'.format(nome.__contains__('Silva')))