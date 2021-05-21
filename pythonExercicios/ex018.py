texto = ' Desafio 018 '
print(' {:*^30}'. format(texto))
from math import radians, cos, sin, tan
angulo = float(input('Informe o ângulo :'))
print('O valor do ângulo informado foi : {} \n'
      'O valor do seno é : {:.2f} \n '
      'o valor do cosseno é : {:.2f} \n '
      'E o valor da tangente é : {:.2f}' .
      format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))