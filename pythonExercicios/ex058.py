from emoji import emojize
from time import sleep
from random import randint

texto = ' \033[1;31mDesafio 058\033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

computador = randint(0, 10)
usuario = 11
palpites = 0
print('''O Computador escolheu um inteiro de \033[31m 0 \033[m à \033[31m 10 \033[m.
Tente adivinhar esse número!''')
while computador != usuario:
    usuario = int(input('Escolha :'))
    print('Processando ',end='')
    for c in range(0,3):
        print('\033[1;33m.', end='\033[m')
        sleep(0.4)
    print('')
    palpites += 1
print('\033[1;36m PARABÉNS VOCE ACERTOU!!!\033[m')
print('{} Computador escolheu: {}'.format(emojize(":thumbsup:", use_aliases=True),computador))
print('Você precisou de \033[1;31m{}\033[m \033[1;36m{}\033[m palpites para acertar!' .format(palpites, emojize(":sunglasses:", use_aliases=True)))