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

#empacotamento de parametros
def contador(*num):
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1



valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
