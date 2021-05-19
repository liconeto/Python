import math

texto = ' Desafio 006 '
print(' {:*^30}'. format(texto))
n = int(input('Digite um número: '))
print(' O valor digitado foi {}.\n Seu dobro é {}. \n Seu triplo é {}. \n E sua raiz quadrada é {}.'. format(n, n * 2, n * 3, math.sqrt(n)))