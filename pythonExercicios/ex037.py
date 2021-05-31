texto = ' Desafio 037 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

print('\033[7;31;40mSistema de conversão Curso em video \033[m')
numero = int(input('Informe um número inteiro para ser convertido :'))
opcao = int(input('Escolha a base de conversão :\n'
                  '\033[1;34m * 1 para binário \n * 2 para Octal \n * 3 para Hexadecimal \033[m\n'))

