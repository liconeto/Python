import datetime

texto = ' Desafio 041 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

print('Confederação Nacional de Natação Curso em Vídeo')
print('A seguir informe a data de nascimento do Atelte :')
data = str((input('data :')))
data = str.replace('-','/', data)
dtn = datetime.datetime.fromisoformat(input('Informe a data de nascimentodo do Atleta :'))

print('Data {}' .format(data))
print('Dia {}' .format(dtn.day))