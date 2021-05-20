texto = ' Desafio 015 '
print(' {:*^30}'. format(texto))
dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
print('Você alugou o carr por {}dias, e rodou {:.2f} kms \n'
      ' O Total a pagar é : R${:.2f}' .format(dias, km, (dias * 60) + (km * 0.15)))
