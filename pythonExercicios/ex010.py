texto = ' Desafio 010 '
print('\033[1;34m {:*^30}\033[m'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}
n = float(input('{}Digite o valor que você tem na carteira:{} {}R${}' .format(cores['cinza'], limpa, cores['verde'], limpa)))
print(' Você tem R$: {:.2f}\n E com esse valor você consegue comprar {}US$: {:.2f}' .format(n, cores['vermelho'], n / 3.27))

