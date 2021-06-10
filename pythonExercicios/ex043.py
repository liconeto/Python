texto = ' Desafio 043 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

print('{}Calculadora IMC Curso em Video{}' .format(cores['ciano'], limpa))
peso = float(input('Informe o seu peso :'))
altura = float(input('Informe sua altura:'))
imc = peso / (altura * 2)

if imc < 18.5:
    print('Você tem o abaixo do peso {}IMC ={:.2f}' .format(cores['ciano'], imc))
elif imc >= 18.5 and imc < 25:
    print('Você está com peso ideal {}IMC =:{:.2f}' .format(cores['verde'], imc))
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso {}IMC ={:.2f}' .format(cores['amarelo'], imc))
elif imc >= 30 and imc < 40:
    print('Você está com obesidade {}IMC ={:.2f}' .format(cores['vermelho'], imc))
else:
    print('Você está com obesidade mórbida {:.2f} IMC = {}' .format(cores['roxo'], imc))

