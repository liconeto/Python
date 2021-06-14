texto = ' Desafio 052 '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 = ' Verificador número primo Curso em Vídeo '
print('{}{:*^50}{}' .format(cores['ciano'], texto2, limpa))

n = int(input('{}Informe um número inteiro :{}' .format(cores['azul'], limpa)))
conta = 0
for c in range(n, 0, -1):
    if n % c == 0:
        conta = conta+1
if conta == 2:
    print('é primo')
else:
    print('Não é primo')
print(conta)