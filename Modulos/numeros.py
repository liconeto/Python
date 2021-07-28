from uteis import numeros
from time import sleep
aula = (' Aula 22 - Funções Módulos e Pacotes ')

print('\033[1;35m{:=^36}\033[m' .format(aula))

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O Triplo de {num} é {numeros.triplo(num)}')
