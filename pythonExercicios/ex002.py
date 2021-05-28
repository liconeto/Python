texto = ' Desafio 002 '
print('\033[1;34m {:*^30}'. format(texto))

nome = input('\033[4;36mQual é o seu nome? :')
print('Olá ', nome,', seja bem-vindo!')
print('Olá, {}, seja bem-vindo!' .format(nome))
