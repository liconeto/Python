from time import sleep
aula = (' Aula 21 - Funções DEF Parte II ')

print('\033[1;34m{:=^36}\033[m' .format(aula))
'''
 * Interactive Help
 * docstring
 * Argumentos opcionais
 * Escopo de variaveis
 * Retorno de resultados'''

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i:início da contagem
    :param f:fim da contagem
    :param p:passo da contagem
    :return:sem retorno
    """
    c =i
    while c<= f:
        print(f'{c}', end='..')
        c += p
        sleep(0.5)
    print('FIM!')


def somar(a=0, b=0, c=0):
    """
    -> Faz a soma com tr~es parâmetros e os mesmos estã odefinidos com parametros opcionais!
    :param a: parâmetro para a soma opcional
    :param b: parâmetro para a soma opcional
    :param c: parâmetro para a soma opcional
    :return: sem retorno
    """
    s = a + b + c
    return s


contador(2, 10, 2)
help(contador)

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os valores das somas são : \033[1;31m{r1}, {r2}, {r3}\033[m')
def teste():
    #Escopo Local
    x= 8
    print(f'Teste N vale: {n}')
    print(f'Teste X vale: {x}')


#Escopo global
n =2
print('ESCOPO de variavel ')
print(f'{n}')
teste()

def fatorial(num =1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O Fatorial de {n} é: {fatorial(n)}')
n1 = fatorial(5)
n2 = fatorial(4)
n3 = fatorial()
print(f'{n1}')
print(f'{n2}')
print(f'{n3}')
