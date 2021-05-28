texto = ' Desafio 033 '
print(' {:*^30}'. format(texto))

print('Informe os números para realizar os calculos!')
n1 = float(input('Informe o primeiro : '))
n2 = float(input('Informe o segundo :'))
n3 = float(input('Informe o terceiro :'))

if n1 > n2 and n1 > n3 and n2 > n3:
    print('é o maior {}, é o do meio {}, é o menor {}' .format(n1, n2, n3))
elif n1 > n2 and n1 > n3 and n3 > n2:
    print('é o maior {}, é o do meio {}, é o menor {}'.format(n1, n3, n2))
elif n2 > n1 and n2 > n3 and n1 > n3:
    print('é o maior {}, é o do meio {}, é o menor {}'.format(n2, n1, n3))
elif n2 > n1 and n2 > n3 and n3 > n1:
    print('é o maior {}, é o do meio {}, é o menor {}'.format(n2, n3, n1))
elif n3 > n1 and n3 > n2 and n1 > n2:
    print('é o maior {}, é o do meio {}, é o menor {}'.format(n3, n1, n2))
else:
    print('é o maior {}, é o do meio {}, é o menor {}'.format(n3, n2, n1))