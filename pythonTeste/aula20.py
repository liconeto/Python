aula = (' Aula 20 - Funções DEF ')

print('\033[1;34m{:=^36}\033[m' .format(aula))

def soma(a, b):
    print(f'A={a} e B={b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print('-' * 20)

# Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(4, 1)