from time import sleep
aula = (' Aula 17 - Listas ')

print('\033[35m{:=^30}\033[m' .format(aula))
tupla = () # tupla de dados
lista = ['Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'] # lista de dados
dicionario = {} # dicionario de dados

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))
for c, v in enumerate(valores):
    print(f'Naposição \033[31m{c}\033[m encontrei o valor \033[32m{v}\033[m!')
    sleep(0.4)
print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
# b = a dessa forma iguala as lista com ligação
b = a[:] # dessa forma copia os dados de uma lista pra outra!
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
