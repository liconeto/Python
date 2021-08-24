lista = [1, 10]
try:

    numero = lista[1]
    x = a = 1
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 0
    #Considerar hierarquia no tratamento de erro:
    print(f'fecha')
    arquivo.close()
except ZeroDivisionError:
    print(f'Não é possivel realizar uma ivisão por 0')
except ArithmeticError:
    print(f'Não foi possivel realizar uma operação aritimetica')
except IndexError:
    print(f'Erro ao acessar um indice invalido da lista!')
except BaseException as ex:
    print(f'{ex}')
else:
    print(f'Executa quando não houve exceção')
finally:
    print(f'Sempre executa!!!')
    arquivo.close()