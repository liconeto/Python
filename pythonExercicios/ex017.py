texto = ' Desafio 017 '
from math import hypot
print(' {:*^30}'. format(texto))
catetoO = float(input('Informeo valor do cateto oposto : '))
catetoA = float(input('Informe o valor do cateto adjacente : '))
hipotenusa = hypot(catetoO, catetoA)
print('O valor do cateto oposto é : {} \n'
      'O valor do cateto adjacente é : {} \n'
      'O valor da hipotenusa é ? {:.2f}' .format(catetoO, catetoA, hipotenusa))
print('Hipotenusa : {:.2f}' .format((catetoO **2 + catetoA **2) ** (1/2) ))
