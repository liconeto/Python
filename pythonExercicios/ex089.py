from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;33m Desafio 089 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[36m Boletim Alunos \033[m '
print(f'{texto2:*^50}')

aluno = list()
sala = list()
continua = 'S'
nraluno = 0
while continua not in 'nN':
    nome = str(input('Digite o nome do Aluno :'))
    n1 = float(input('A 1ª nota :'))
    n2 = float(input('A 2ª nota :'))
    media = (n1 + n2) / 2
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    aluno.append(media)
    sala.append(aluno[:])
    aluno.clear()
    continua = str(input('Deseja cadastrar mais alunos : [S/N]'))
print('-=' * 30)
print('Nº NOME                 MÉDIA')
print('-' * 30)
for i, c in enumerate(sala):
    print(f'{i}  {c[0]:<20} {c[3]}')
print('-' * 30)

while nraluno != 999:
    nraluno = int(input('Mostrar as notas de qual aluno? (999 para interromper):'))
    for i, c in enumerate(sala):
        if i == nraluno:
            print(f'Notas de {c[0]} |{c[1]} e {c[2]} |')
print('Finalizando', end='')
for c in range(0,6):
    sleep(0.3)
    print('\033[33m.\033[m', end='')
print()
print('<<< Volte sempre! >>>')