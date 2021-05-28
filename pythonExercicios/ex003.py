texto = ' Desafio 003 '
print('\033[1;34m {:*^30}'. format(texto))

n1 = int(input('\033[32mDigite um número: '))
n2 = int(input('\033[35mDigite outro número: '))
s = n1 + n2
print('\033[31mA soma entre {} e {} é = {}' .format( n1, n2, s))
