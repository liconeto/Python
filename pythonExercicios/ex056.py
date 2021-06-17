from emoji import emojize
from time import sleep
from datetime import date

texto = ' Desafio 056 '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

sidade = 0
hvelho =''
hidade =0
m20 =0
for c in range(0,4):
    nome = str(input('\033[34m Informe o nome :'))
    idade = int(input('\033[36m Informe a idade :'))
    sexo = int(input('Informeo sexo : 1 = Feminico | 2 = Masculino :'))

    sidade += idade
    if c == 1 and sexo == 2:
        hvelho = nome
        hidade = idade
    if sexo == 1 and idade < 20:
      m20 + 1
    if sexo == 2 and hidade < idade:
        hvelho =nome
        hidade = idade

print('A média de idade do grupo é : {}' .format( sidade / 4))
print('O Homem mais velho é : {}'. format(hvelho))
print('E temos {} mulheres com menos de 20 anos ' .format(m20))