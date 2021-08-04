def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except(ValueError, TypeError):
            print('\033[1;31mValor Inválido, digite um número inteiro!\033[m')
        except KeyboardInterrupt:
            print('\033[31m O usuário preferiu não informar esses dados!')
            return 0
        else:
            return inteiro


def linha(tam=42):
    print('-' * tam)


def cabecalho(txt):
    linha()
    print(f'| {txt.center(38 )} |')
    linha()


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f' \033[1;31m{c}\033[m - \033[34m{item}\033[m ')
        c += 1
    linha()
    opc = leiaInt('Sua Opção: ')
    return opc
