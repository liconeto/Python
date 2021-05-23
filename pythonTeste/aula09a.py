aula = ('Aula 09')
print('{:=^30}' .format(aula))

frase = 'Curso em Video Python'

print(frase[:14])
print(frase[::2])
print('len : ', len(frase))
print('count : ', frase.count('o'))
print('find : ', frase.find('deo'))
print('in : ', 'Curso' in frase)
print('replace : ', frase.replace('Python', 'Android'))
print('UPPER : ', frase.upper())
print('lower : ', frase.lower())
print('capitalize : ', frase.capitalize())
print('title : ', frase.title())
print('strip : ', frase.strip())

print('split : ', frase.split())
dividio = frase.split()
print('split : ', dividio[3][1])
print('join : ', '-'.join(frase))
