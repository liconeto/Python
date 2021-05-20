texto = ' Desafio 012 '
print(' {:*^30}'. format(texto))
preco = float(input('Digite o valor do produto: '))
print(' O valor do produto é : {:.2f}\n Porem o gerente está dando 5% de desconto, desconto : {:.2f}\n'
      ' Produto com o desconto é: {:.2f}' .format(preco, preco * 0.05, preco - (preco * 0.05)))