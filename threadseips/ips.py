import ipaddress

# Manipulando Ip´s

ip = '192.168.0.1'
endereco = ipaddress.ip_address(ip)
print('Trabalhando com ip:')
print(endereco + 1000)

ip2 = '192.168.0.0/24'
rede = ipaddress.ip_network(ip2, strict=False)
print('Trabalhando com rede:')
for ip in rede:
    print(ip)