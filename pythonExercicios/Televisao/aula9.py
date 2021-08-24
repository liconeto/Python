
def escrever_arquivo(texto):
    arquivo = open('teste.txt','w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for aluno in aluno_nota:
        lista_notas = aluno.split(',')
        alunoN = lista_notas[0]
        print(alunoN)
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
        #print(media(lista_notas))

if __name__ == '__main__':
    lista_media = media_notas('notas.txt')
    print(lista_media)
    #escrever_arquivo('Primeira linha. \n')
    #aluno = '\nCesar,7,9,3,8'
    #atualizar_arquivo('notas.txt',aluno)
    #ler_arquivo('teste.txt')