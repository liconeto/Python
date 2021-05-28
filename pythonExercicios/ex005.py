texto = ' Desafio 006 '
print('\033[1;34m {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

n = int(input('Digite um número: '))
print('O número digitado foi {}{}{}, seu antecessor é {}{}{}, e seu sucessor é {}{}{} '.format(cores['cinza'], n, limpa, cores['vermelho'],n - 1, limpa, cores['verde'], n + 1, limpa))
