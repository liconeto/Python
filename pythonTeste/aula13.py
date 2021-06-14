aula = ('Aula 13')
print('{:=^30}' .format(aula))

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print("FIM")

#for c in range(6, 0, -1):
#    print(c)
#print('FIM')