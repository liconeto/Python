from time import sleep
aula = (' Aula 19 - Dicionarios ')

print('\033[1;36m{:=^36}\033[m' .format(aula))

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O estado {k} é {v}')