texto = ' Desafio 032 '
print(' {:*^30}'. format(texto))

ano = int(input('informe o ano : '))

if ano % 4 == 0 and ano % 100 != 0:
    print('resto divisão {}' .format(ano % 4))
    print('resto divisão {}'.format(ano % 100))