import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

#construtor com o tipo de criptografia do hash
hash1 = hashlib.new('ripemd160')
#atualizado o hash com os dados contidos no arquivo
hash1.update(open(arquivo1, 'rb').read())

#construtor com o tipo de criptografia do hash
hash2 = hashlib.new('ripemd160')
#atualizado o hash com os dados contidos no arquivo
hash2.update(open(arquivo2, 'rb').read())

#Comparando os hashs
if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquibo b.txt é: ', hash2.hexdigest())
else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquibo b.txt é: ', hash2.hexdigest())

