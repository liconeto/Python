alunos = open("C:\database\Alunos.dat","r")
linha = alunos.readline()
while linha:
    valores = linha.split()
    print('QB ', valores[0], valores[1], 'obteve a avaliacao ', valores[4] )
    linha = alunos.readline()

ref_arquivo.close()
        

