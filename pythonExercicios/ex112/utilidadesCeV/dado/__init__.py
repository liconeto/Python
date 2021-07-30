
def leiaDinheiro():
    """
    -> Função para leitura de valores com validação de dados
    :return: valor float para calculo
    """

    while True:
        try:
            lido = str(input('Digite o Valor R$: '))
            valor = float(lido.replace(',','.'))
        except:
            print(f'\033[31mERRO Valor {lido} é inválido, Digite um valor monetário R$ :\033[m')
        else:
            break

    return valor


def leiaInt():

    while True:
        try:
            pct = int(input('Digite a porcentagem :'))
        except:
            print('\33[31mValor inválido, informe um valor inteiro!\033[m')
        else:
            break
    return pct