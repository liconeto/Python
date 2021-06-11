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
print('Data nascimento ={}' .format(dtn.date().strftime("%d/%m/%Y")))
print('Hoje é {}' .format(hoje.strftime("%d/%m/%Y")))
idade = ((hoje - dtn).days / 365)
print('{:.0f}' .format((hoje - dtn).days / 365))

if idade <= 9:
    print('O atleta tem {}{:.0f}{} anos e é da {}categoria Mirim' .format(cores['ciano'], idade,'\033[m', cores['vermelho']))
elif idade >9 and idade <= 14:
    print('O atleta tem {}{:.0f}{} anos e é da {}categoria Infantil' .format(cores['vermelho'], idade, '\033[m', cores['amarelo']))
elif idade >14 and idade <= 19:
    print('O Atleta tem {}{:.0f}{} anos e é da {}categoria Junior' .format(cores['azul'], idade, '\033[m', cores['roxo']))
elif idade >= 20 and idade <= 25:
    print('O Atleta tem {}{:.0f}{} anos e é da {}categoria Sênior' .format(cores['cinza'], idade, '\033[m', cores['vermelho']))
else: print('O Atleta tem {}{:.0f}{} e é da categoria Master' .format(cores['vermelho'], idade, '\033[m', cores['ciano']))