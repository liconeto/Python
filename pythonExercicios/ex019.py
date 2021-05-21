import random

texto = ' Desafio 019 '
print(' {:*^30}'. format(texto))
aluno1 = input('Informe o nome do primeiro aluno :')
aluno2 = input('Informe o nome do segundo aluno :')
aluno3 = input('Informe o nome do terceiro aluno :')
aluno4 = input('Informe o nome do quarto aluno :')
lista = [aluno1, aluno2, aluno3, aluno4]

print('O sorteado foi : {}'.format(random.choice(lista)))