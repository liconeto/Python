texto = ' Desafio 040 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

print('{}Calculador de média Curso em Vídeo! \033[m' .format(cores['azul']))

n1 = float(input('Informe a primeira nota :'))
n2 = float(input('Informe a segunda nota :'))

media = (n1 + n2) / 2

if media < 5:
    print('{}Sua média {}. VOcê está REPROVADO!' .format(cores['vermelho'],media))
elif media >= 5 and media <= 6.9:
    print('{}Sua média foi {}. Você está em RECUPERAÇÃO' .format(cores['amarelo'], media))
else:
    print('{}Sua média foi {}. Você está APROVADO!!' .format(cores['ciano'], media))
