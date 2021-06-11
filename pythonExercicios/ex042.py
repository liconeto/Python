texto = ' Desafio 042 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

print('\033[31mPrincipio da desigualdade triangular!\033[m')
print('Para saber se é possivel formar o Triângulo, informe 3 retas ')
ab = float(input('Primeira reta : '))
cd = float(input('Segunda reta : '))
ef = float(input('Terceira reta : '))

if ab + cd > ef and cd + ef > ab and ab + ef > cd:
    print('A soma de duas retas são maiores que a terceira: \n'
          'soma r1 + r2 ={} > r3 = {}' .format(ab + cd, ef))
    print('A soma de duas retas são maiores que a terceira: \n'
          'soma r3 + r2 ={} > r1 = {}'.format(cd + ef, ab))
    print('A soma de duas retas são maiores que a terceira: \n'
          'soma r1 + r3 ={} > r2 = {}'.format(ab + ef, cd ))
    print('É POSSIVEL MONTAR UM TRIÂNGULO')
    if ab == cd == ef:
        print('É um triângulo {}Equilátero' .format(cores['vermelho']))
    elif ab == cd or ab == ef or cd == ef:
        print('É um triângulo {}Isóceles' .format(cores['ciano']))
    else:
        print('É um triângulo {} Escaleno' .format(cores['roxo']))
else:
    print('{}Não é possivel formar o triângulos' .format(cores['vermelho']))