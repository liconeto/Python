import json
from urllib import request

texto = ' \033[1;35m Desafio Moedas \033[m '
print('{:*^50}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

texto2 =' \033[34m Função cota moedas \033[m '
print(f'{texto2:*^50}')

requisicao = request.urlopen("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda='EUR'&@dataCotacao='08-17-2021'&$top=100&$skip=0&$format=json&$select=cotacaoVenda,tipoBoletim")
cotacao = requisicao.read()
jsonV = json.loads(cotacao.decode("utf-8"))
dados = json.decoder(jsonV)
print(f'{requisicao}')
print(f'{cotacao}')
print(f'{jsonV}')
print(f'{dados}')