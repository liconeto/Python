import random
import string

#Gerador de senhas Python
#tamanho da senha
# tamanho = 16
tamanho = int(input('Informe a quantidade de caracteres que desja: '))

# caracteres que irão compor a senha
chars = string.ascii_letters + string.digits + '!@#$%¨&*()-+=,.;:/?' #Todas as letras
#chars = string.ascii_lowercase + string.digits + '!@#$%¨&*()-+=,.;:/?' só letras minusculas
#chars = string.ascii_uppercase + string.digits + '!@#$%¨&*()-+=,.;:/?' Só letras maiusculas


#randomica que armazenará a senha
rnd = random.SystemRandom() #os.urandom

#senha gerada
senha = ''.join(rnd.choice(chars) for i in range(tamanho))
print(f'A senha gerada foi : {senha}')