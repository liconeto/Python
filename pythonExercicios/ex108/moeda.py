def aumentar(num=0, pct=0):
    vlrMaior = 0
    vlrMaior = (num + ((num * pct) / 100))
    return vlrMaior


def diminuir(num=0, pct=0):
    vlrMenor = 0
    vlrMenor = (num -((num * pct) / 100))
    return vlrMenor


def metade(num=0):
    vlrmetade = 0
    vlrmetade = num / 2
    return vlrmetade


def dobro(num=0):
    vlrdobro = 0
    vlrdobro = num * 2
    return vlrdobro


def moeda(num=0, moeda='R$'):
    valor = 0
    return f'{moeda}{num:>8.2f}'.replace('.',',')
