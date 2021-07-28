from builtins import print
from datetime import date
from emoji import emojize
from time import sleep
from random import randint
from operator import itemgetter

texto = ' \033[1;37m Desafio 105 \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[36m Função Notas Mult \033[m '
print(f'{texto2:*^50}')

def notas(*valores, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param valores: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou naos adicionar a situação
    :return: dicionário com várias informações da turma
    """
    nums = valores
    cont = 0
    maior = 0
    menor = 0
    soma = 0
    media = 0
    informacoes =dict()
    print(f'{nums}')
    for i, v in enumerate(nums):
        print(f'Indice{i} e valor{v}')
        cont +=1
        soma += v
        if i == 0:
            menor = v
            maior = v
        if menor > v:
            menor = v
        if maior < v:
            maior = v
    media = soma / cont
    if media < 5:
        situacao = 'ruim'
    elif 5 <= media < 7:
        situacao = 'RAZOAVEL'
    else:
        situacao = 'BOA'

    if sit:
        informacoes = {'total': cont, 'menor': menor, 'maior': maior, 'media': media, 'situação': situacao}
    else:
        informacoes = {'total': cont, 'menor': menor, 'maior': maior, 'media': media}
    return informacoes
def notas2(*valores, sit=False):
    """
        -> Função para analisar notas e situações de vários alunos.
        :param valores: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou naos adicionar a situação
        :return: dicionário com várias informações da turma
        """
    r=dict()
    r['total'] = len(valores)
    r['maoir'] = max(valores)
    r['menor'] = min(valores)
    r['media'] = sum(valores) / len(valores)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'Razoavel'
        else:
            r['situacao'] = 'RUIM'
    return r



resp =notas(10, 5, 6, 10, 7, sit=True)
print(f'{resp}')
help(notas)
resp2 = notas2(10, 5, 6, 10, 7, sit=True)
print(f'{resp2}')
help(notas2)
