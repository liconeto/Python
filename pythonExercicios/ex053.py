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

frase = str(input('Digite uma frase :')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

rfrase = ''
inverso =junto[::-1]
for letra in range(len(junto) - 1, -1, -1):
    rfrase += junto[letra]

if junto == rfrase:
    print('é um palindromo')
else:
    print('Não é um palindromo')

print('\033[35m'+junto, '\033[36m'+rfrase)
print('Inverso {}{}' .format(cores['vermelho'], inverso))