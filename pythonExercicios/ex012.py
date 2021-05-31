texto = ' Desafio 012 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

preco = float(input('\033[4;30;46m Digite o valor do produto: \033[m'))
print(' O valor do produto é : {}{:.2f}{}\n Porem o gerente está dando 5% de desconto, desconto : {}{:.2f}{}\n'
      ' Produto com o desconto é: {}{:.2f}{}' .format(cores['verde'], preco, limpa, cores['vermelho'], preco * 0.05,limpa , cores['azul'],preco - (preco * 0.05),limpa ))