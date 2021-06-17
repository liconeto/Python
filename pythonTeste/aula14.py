aula = ('Aula 14')
print('{:=^30}' .format(aula))

'''r = 'S'
while r == 'S':
    n = int(input('DIgite o valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('FIM !')
'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('''Você digitou \033[36m{}\033[m números pares.
 E \033[31m{}\033[m números ímpares!''' .format(par, impar))