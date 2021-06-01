texto = ' Desafio 038 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

print('Comparação de 2 valores Curso em vídeo')
n1 = float(input('{}Informe o primeiro número :{}' .format(cores['ciano'], limpa)))
n2 = float(input('{}Informe o segundo número :{}'.format(cores['azul'], limpa)))

if n1 > n2:
    print('{}O primeiro é maior :{}' .format(cores['vermelho'], n1))
elif n2 > n1:
    print('{} O segundo é maior :{}' .format(cores['roxo'], n2))
else:
    print('{}Eles são iguais : {}={}' .format(cores['amarelo'], n1, n2))
