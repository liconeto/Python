texto = ' Desafio 012 '
print(' {:*^30}'. format(texto))
preco = float(input('Digite o valor do produto: '))
print(' O valor do produto é : {}\n Porem o gerente está dando 5% de desconto, desconto : {}\n'
      ' Produto com o desconto é: {}' .format(preco, preco * 0.05, preco - (preco * 0.05)))