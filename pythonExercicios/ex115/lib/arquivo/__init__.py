

def arquivo():
    narquivo ='cursoemvideo.txt'
    try:
        arquivo = open(narquivo, 'r+')
        print('Arquivo aberto!')
    except FileNotFoundError:
        arquivo = open(narquivo, 'w+')
        print('Arquivo craido com sucesso!')
    return narquivo



def lerArquivo():
    nomeArq = arquivo()
    abrir = open(nomeArq, 'r+')
    for linhas in abrir:
        valores = linhas.split()
        print(f'{valores}')


def escreveArquivo(dado):
    nomeArq = arquivo()
    abrir = open(nomeArq, 'at+')
    abrir.write(dado)
    abrir.close()
