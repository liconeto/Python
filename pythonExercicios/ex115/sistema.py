from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep
arquivo()
while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resp == 1:
        cabecalho('Opção 1')
        lerArquivo()
    elif resp == 2:
        cabecalho('Opção  2')
        dado =str(input('Informe nome ; idade: '))
        escreveArquivo(dado+'\n')
    elif resp == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida!\033[m')
    sleep(2)

