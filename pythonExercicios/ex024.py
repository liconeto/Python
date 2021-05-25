texto = ' Desafio 024 '
print(' {:*^30}'. format(texto))
cidade = str(input('Digite o nome da cidade : ')).strip()

cidade = cidade.split()

print('A cidade digiatada foi : {} \n'
      'e ela começa com : {} \n'
      'é igual a SANTOS : {} '. format(cidade, cidade[0], cidade[0] == 'SANTO'))