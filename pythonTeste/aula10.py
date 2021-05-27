aula = ('Aula 09')
print('{:=^30}' .format(aula))
'''
nome =str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Sedu nome é tão normal!')
print('Bom dia, {}' .format(nome))
'''

n1 = float(input('Digite a primeira nota : '))
n2 = float(input('Digite a segunda nota : '))
m = (n1 + n2) /2

print('A sua média foi {:.1f}' . format(m))
if m >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

print('***PARABéNS***' if m >= 6.0 else " ***ESTUDE MAIS*** ")