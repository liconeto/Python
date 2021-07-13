from time import sleep
aula = (' Aula 18 - Listas ')

print('\033[35m{:=^30}\033[m' .format(aula))

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
    #galera.append(teste) cópia de dados da lista com ligação
galera.append(teste[:]) #cópia de dados da lista sem ligação
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
galeras = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45], ['Mariana', 7]]
print(galeras)
print(galeras[0][0])
print(galeras[4])