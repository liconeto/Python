def aumentar(num=0, pct=0, formata=False):
    """
    ->Função para aumentar o valor porcentualmente!
    :param num: valor que será aumentado porcentualmente
    :param pct: porcentagem %
    :param formata: parâmetro opicional de formatação, se será ou não formatado valor default False
    :return: retorno do valor calculado
    """
    vlrMaior = 0
    vlrMaior = (num + ((num * pct) / 100))
    return vlrMaior if formata is False else moeda(num=vlrMaior)


def diminuir(num=0, pct=0, formata=False):
    """
    -> Função para diminuir porcentualemnte o valor informado
    :param num: valor base de calculo que será diminuido
    :param pct: porcentagem que devara diminuir o valor base
    :param formata: parâmetro opicional de formatação, se será ou não formatado valor default False
    :return: retorno do valor calculado
    """
    vlrMenor = 0
    vlrMenor = (num -((num * pct) / 100))
    return vlrMenor if formata is False else moeda(num=vlrMenor)


def metade(num=0, formata=False):
    """
    ->Função para calcular a metada do valor informado
    :param num:valor base
    :param formata: parâmetro opicional de formatação, se será ou não formatado valor default False
    :return: retorno do valor calculado
    """
    vlrmetade = 0
    vlrmetade = num / 2
    return vlrmetade if formata is False else moeda(num=vlrmetade)


def dobro(num=0, formata=False):
    """
    -> Função para calcular o dobro do valor informado
    :param num: valor base de calculo
    :param formata: parâmetro opicional de formatação, se será ou não formatado valor default False
    :return: retorno do valor calculado
    """
    vlrdobro = 0
    vlrdobro = num * 2

    return vlrdobro if formata is False else moeda(num=vlrdobro)


def moeda(num=0, moeda='R$'):
    """
    -> Função de formataçãoa de valores
    :param num: parametro base
    :param moeda: parametro de moeda valor default R$
    :return: moeda formatada com , no lugar do . e R$
    """
    valor = 0
    return f'{moeda}{num:>8.2f}'.replace('.',',')


def resumo(num=0, pctS=10, pctD=5):
    """
    -> Função de resumo de calculos de outras funções!
    :param num: valor base de calculo
    :param pctS: porcentagem de aumento, default 10%
    :param pctD: porcentagem de redução, default 5%
    :return: sem retorno valores impressos na tela
    """
    vlDobro = dobro(num, True)
    vlrMetade =metade(num, True)
    vlrMaior = aumentar(num, pctS, True)
    vlrMenor = diminuir(num, pctD, True)
    print('-' * 40)
    resumo = 'RESUMO DO VALOR'
    print(f'{resumo:^40}')
    print('-' * 40)
    print(f'Preço Analisado: \033[1;31m{moeda(num):>22}\033[m')
    print(f'Dobro do Preço : \033[34m{vlDobro:>22}\033[m')
    print(f'Metade do preço: \033[34m{vlrMetade:>22}\033[m')
    print((f'{pctS}% de aumento : \033[34m{vlrMaior:>22}\033[m'))
    print(f'{pctD}% com redução: \033[34m{vlrMenor:>22}\033[m')
    print('-' * 40)
