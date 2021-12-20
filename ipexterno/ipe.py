import re
import json
from urllib.request import urlopen


url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']
print(f'Detalhes do IP Externo ')
print(f'IP: {ip} Regiao: {regiao} \nPaís: {pais} Organização: {org}')