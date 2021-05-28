texto = ' Desafio 032 '
print(' {:*^30}'. format(texto))
from datetime import date

ano = int(input('informe o ano : Coloque 0 para analisar o ano atual :'))
if ano == 0: ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400== 0:
    print('resto divisão {}' .format(ano % 4))
    print('resto divisão {}'.format(ano % 100))
    print('É Bissexto !')
else:
    print('Não é Bissexto !')