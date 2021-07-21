from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint
from operator import itemgetter

texto = ' \033[1;31m Desafio 095 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[32m Aproveitamento Jogador aprimorado \033[m '
print(f'{texto2:*^50}')
partidas = total =0
jogadores = list()
jogador = dict()
gols= list()
while True:
    nome = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    for i in range(1, partidas+1):
        while True:
            try:
                gols.append(int(input(f'  * Quantos gols na partida {i}: ')))
            except:
                print('Valor inválido, digite um número inteiro!')
            else:
                break
    for i, c in enumerate(gols):
        total += c
    print('+*' * 30)
    jogador= {'nome': nome, 'gols': gols[:], 'total': total}
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    total =0
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break

print(f'{jogadores}')
print('*+' * 30)
print('Cod Nome        Gols          Total')
print('-' * 40)
for k, v in enumerate(jogadores):
    print(f'\033[1;31m{k:>3}\033[m {v["nome"]:<12}{v["gols"]}{v["total"]:>7}')
print('-' * 40)

while True:
    while True:
        try:
            detalhe = int(input('Quer mostrar os dados de qual jogador? (\033[1;31m999\033[m para parar) '))
        except:
            print('Valor inválido!')
        else:
            break
    if detalhe == 999:
        break
    for i, v in enumerate(jogadores):
        if detalhe == i:
            print(f'Levantamento do jogador \033[1;31m{v["nome"]}\033[m: ')
            for i,c in enumerate(v["gols"]):
                print(f'   No jogo {i+1} fez \033[33m{c}\033[m gols.')
print('+*' * 30)
print('<<< \033[35mVolte sempre !\033[m >>>')