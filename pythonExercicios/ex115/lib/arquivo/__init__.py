<<<<<<< HEAD
from files import *

try:
    arq = open('cursoemvideo.txt', 'r+')
except FileNotFoundError:
    arq = open('cursoemvideo.txt', 'w+')
else:
    arq.close()
=======
>>>>>>> dec42ce38ea86837b5fa96714d30ec149361c45f


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
<<<<<<< HEAD
        valores = linhas.split(';')
        valores[1] = valores[1].replace('\n', '')
        print(f'| {valores[0]:<30}{valores[1]:>8} |')
=======
        valores = linhas.split()
        print(f'{valores}')
>>>>>>> dec42ce38ea86837b5fa96714d30ec149361c45f


def escreveArquivo(dado):
    nomeArq = arquivo()
    abrir = open(nomeArq, 'at+')
    abrir.write(dado)
    abrir.close()
