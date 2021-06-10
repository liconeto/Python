import random

texto = ' Desafio 045 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}
print('{}JokenPo Curso em Vídeo{}' .format(cores['roxo'], limpa))

opcao = int(input('Escolha a opção:\n'
                    '| 1 - Pedra | 2 - Papel | 3 - Tesoura |'))
jogador =''

if opcao == 1:
    jogador = 'Pedra'
elif opcao == 2:
    jogador = 'Papel'
else:
    jogador = 'Tesoura'

computador = random.choice(['Pedra', 'Papel', 'Tesoura'])

if jogador == computador:
    print('Houve um empate você escolheu :{} e o computador escolheu : {}' .format(jogador, computador))
elif jogador == 'Pedra' and computador == 'Tesoura':
    print('O jogador venceu ele escolheu {} e o computador escolheu {}' .format(jogador, computador))
elif jogador == 'Papel' and computador =='Pedra':
    print('O jogador venceu ele escolheu {} e o computador escolheu {}'.format(jogador, computador))
elif jogador == 'Tesoura' and computador == 'Papel':
    print('O jogador venceu ele escolheu {} e o computador escolheu {}'.format(jogador, computador))
else:
    print('O Computador venceu ele escolheu {} e o jogador escolheu {}'.format(computador, jogador))
print('computador ={}'.format(computador))
print(jogador)
