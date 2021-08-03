def linha():
    print('-' * 42)


def menu():
    linha()
    menuP = 'MENU PRINCIPAL'
    print(f'| {menuP:^38} |')
    linha()
    print('| 1 - \033[34mVer pessoas cadastradas\033[m            |')
    print('| 2 - \033[34mCadastrar nova pessoa\033[m              |')
    print('| 3 - \033[34mSair do Sistema \033[m                   |')
    linha()
    while True:
        try:
           opcao = int(input('\033[32mSua Opção :\033[m'))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número inteiro válido!')
        if opcao == 1 or opcao == 2 or opcao == 3:
            break
        else:
            print(f'\033[1;31m Erro: Digite uma opção válida! Opção escolhida:{opcao}')
            continue
    return opcao