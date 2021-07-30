from time import sleep
aula = (' Aula 23 - Tratamento de Erros e Exceções ')

print('\033[1;35m{:=^36}\033[m' .format(aula))

try:
    a = int(input('Numerador :'))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('VOLTE SEMPRE MUITO OBRIGADO!')