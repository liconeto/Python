texto = ' Desafio 028 '
print(' {:*^30}'. format(texto))
from random import randint
from time import sleep
print('-=-' * 25)
ni = randint(0, 5)
nd = int(input('Tente adivinhar o número que o computador pensou! \n'
               'Digite um número entre 0 e 5 : '))
print('-=-' * 25)
print('Processando ...')
sleep(3)
print('Número que o Computador pensou : {}' .format(ni))
print('Número digitado : {}' .format(nd))

if ni == nd:
    print('Você acertou! : {} e {} são iguais!' .format(ni, nd))
else:
    print('Você errou " : {} e {} são diferentes!' .format(ni, nd))
