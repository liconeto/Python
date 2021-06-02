import datetime

texto = ' Desafio 041 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

print('Confederação Nacional de Natação Curso em Vídeo')
print('A seguir informe a data de nascimento do Atleta :')
dia = input('Informe o dia :')
mes = input('Informe o mês :')
ano = input('Informe o ano :')

dtn = datetime.datetime.fromisoformat((ano+'-'+mes+'-'+dia))
hoje = datetime.datetime.today()
print('Data {}' .format(dtn.date().strftime("%d/%m/%Y")))
print('Hoje é {}' .format(hoje.strftime("%d/%m/%Y")))
print('{}' .format((hoje - dtn).strftime("%y")))
