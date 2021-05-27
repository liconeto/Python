texto = ' Desafio 028 '
print(' {:*^30}'. format(texto))
import random

ni = random.randint(0, 5)
nd = int(input('Tente adivinhar o númeor que o computador pensou \n'
               'Digite um número entre 0 e 5 : '))
print('Número que o Computador pensou : {}' .format(ni))
print('Número digitado : {}' .format(nd))

if ni == nd: print('Você acertou! : {} e {} são iguais!' .format(ni, nd))
else: print('Você errou " : {} e {} são diferentes!' .format(ni, nd))