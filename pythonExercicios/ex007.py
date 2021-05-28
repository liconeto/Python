texto = ' Desafio 007 '
print('\033[1;34m {:*^30}\033[m'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}
n1 = float(input('\033[4;40mDigite a primeira nota :\033[m'))
n2 = float(input('\033[4:47mDigite a segunda nota: \033[m'))
print('{} A primeira nota é : {} \n A segunda nota é : {} \n A média é : {:.2F}' .format(cores['roxo'],n1, n2, (n1 + n2)/ 2))