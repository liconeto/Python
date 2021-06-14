from emoji import emojize
from time import sleep
from random import randrange

texto = ' Desafio 053 '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}
texto2 = ' Verificador de palindromo '
print('{}{:=^40}{}' .format(cores['ciano'], texto2, limpa))

frase = input('Digite uma frase :').replace(' ', '')
frase.split()
rfrase = ''

for c in range(len(frase), 0, -1):
    rfrase = rfrase + frase[ c - len(frase) ]
    print(rfrase)

if frase == rfrase:
    print('é um palindromo')
else:
    print('Não é um palindromo')

print(frase)
print(rfrase)