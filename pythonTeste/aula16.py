aula = (' Aula 16 - Tuplas ')
print('\033[35m{:=^30}\033[m' .format(aula))
tupla = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') # tupla de dados
lista = [] # lista de dados
dicionario = {} # dicionario de dados

print(sorted(tupla))

for pos, c in enumerate(tupla):
    print(f'Comerei {c} na vez {pos}')

for comida in range(0, len(tupla)):
    print(f'Vou comer {tupla[comida]} na posição {comida}')

a = (2, 5, 4)
b = (5, 8, 1,2)
c = b + a
print(c.count(5))
print(c.index(8))