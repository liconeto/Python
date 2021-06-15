from emoji import emojize

texto = ' Desafio 048 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

print('Soma dos multiplos de {}3{} no range de 0 à 500 {}{}{}' .format(cores['verde'], limpa, cores['ciano'],emojize(":snowflake:"), limpa))
cont = 0
s = 0
for c in range(0, 500, 3):
   if c % 2 != 0:
       cont = cont + 1
       s = s + c
       print('Impar e multiplo de 3 {}{}{} a soma {}{}{}' .format(cores['vermelho'], c, limpa, cores['roxo'], s, limpa))
print('Soma dos {} números é = {}' .format(cont, s))