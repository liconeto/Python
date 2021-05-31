texto = ' Desafio 013 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

salario = float(input('\033[1;37m Digite o valor do salário: '))
print(' O salário informado foi : {}{}{}\n O aumento consedido é de 15% : {}{}{}\n O salário com o aumento é : {}{}{}'
      '' .format(cores['azul'], salario, limpa, cores['verde'], salario * 0.15, limpa, cores['amarelo'], salario + (salario * 0.15 ), limpa))
