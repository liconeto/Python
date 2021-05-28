texto = ' Desafio 035 '
print(' {:*^30}'. format(texto))
print('Principio da desigualdade triangular!')
print('Para saber se é possivel calcular o Triângulo, informe 3 retas ')
ab = float(input('Primeira reta : '))
cd = float(input('Segunda reta : '))
ef = float(input('Terceira reta : '))

if ab + cd > ef and cd + ef > ab:
    print('A soma de duas retas são maiores que a terceira: \n'
          'soma r1 + r2 ={} > r3 = {}' .format(ab + cd, ef))
    print('A soma de duas retas são maiores que a terceira: \n'
          'soma r3 + r2 ={} > r1 = {}'.format(cd + ef, ab))
    print('A soma de duas retas são maiores que a terceira: \n'
          'soma r1 + r3 ={} > r2 = {}'.format(ab + ef, cd ))
    print('É POSSIVEL MONTAR UM TRIÂNGULO')