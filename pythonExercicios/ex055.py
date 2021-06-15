from emoji import emojize
from time import sleep
from datetime import date

texto = ' Desafio 055 '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}
texto2 =' Comparador de peso Curso em Vídeo '

print('{}{:¨^50}{}' .format(cores['ciano'], texto2, limpa))

maior =0
menor =10000
print('Informe o peso de 5 pessoas para verificar o peso de 5 pessoas')

for c in range(0, 5):
    print('Maior = {} | Menor = {}' .format(maior, menor))
    peso = int(input('Informe o peso para verificação :'))
    if peso > maior:
        maior = peso

    elif peso < menor:
        menor = peso
print('''
O maior peso é = {}{}{}
O menor peso é ={}{}{}''' .format(cores['vermelho'], maior, limpa, cores['ciano'], menor, limpa))