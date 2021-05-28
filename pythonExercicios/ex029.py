texto = ' Desafio 029 '
print(' {:*^30}'. format(texto))
velocidade = float(input('Informe a velocidade do carro : '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(' Você foi multado! \n'
          ' O limite da via é de 80km/h \n E você estava há {}km/h'
          '\n o Valor da sua multa é de R${:.2f}' .format(velocidade, multa))
print('Velocidade permitida! \n'
            'Tenha um bom dia e dirija com cuidado!')