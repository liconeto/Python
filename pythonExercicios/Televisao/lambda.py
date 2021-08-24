contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a+b
subtracao = lambda a, b: a-b

print(f'{soma(5,10)}')
print(f'{subtracao(10, 5)}')
'''Função Lambda (função anonima)'''
calculadora = {
    'soma': lambda a, b: a+b,
    'subtracao': lambda a, b: a-b,
    'multiplicacao': lambda a, b: a*b,
    'divisao': lambda a, b: a/b,
}

print(type(calculadora))
soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']
print(f'{soma(12,4)}')
print(f'{multiplicacao(3,5)}')