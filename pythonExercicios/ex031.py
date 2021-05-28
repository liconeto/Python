texto = ' Desafio 031 '
print(' {:*^30}'. format(texto))

print('Olá, que bom te-lo conosco!')
distancia = float(input('Informe a distância da viagem em Kms : '))
if distancia <= 200 :
    distancia = distancia * 0.50
    print('Sua viagem custará : R${:.2f}' .format(distancia))
else:
    distancia = distancia * 0.45
    print('Sua viagem custará : R${:.2f}'.format(distancia))