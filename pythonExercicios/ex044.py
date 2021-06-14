texto = ' Desafio 044 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

print('{} Condições de pagamento Curso em Vídeo {}' .format(cores['azul'], limpa))
print(' 1 -à vista dinheiro/cheque : 10% de desconto\n'
      ' 2 -à vista no cartão:5% de desconto\n'
      ' 3 -em até 2x no cartão preço normal\n'
      ' 4 -3x ou mais no cartão: 20% de juros.')
op = int(input('{}Escolha a opção de pagamento :' .format(cores['ciano'])))
vprod = float(input('{}Informe o valor do produto :' .format(cores['verde'])))

if op == 1:
    print('Opção {} escolhida, você tem {}10% de desconto = {}, pagará R${:.2f} ' .format(op, cores['verde'], ((vprod * 10) / 100), vprod - ((vprod * 10) / 100)))
elif op == 2:
    print('Opção {} escolhida, você tem {}5% de desconto = {}, pagará R${:.2f} ' .format(op, cores['azul'], ((vprod * 5)/100), vprod-((vprod * 5)/100)))
elif op == 3:
    print('Opção {} escplhida, você pagará em {}2 vezes no cartão R${:.2f} ' .format(op, cores['cinza'], (vprod / 2)))
elif op == 4:
    print('Opção {} escolhida, você pagará em {}3 vezes no cartão com acrescimo de 20% = {:.2f}, pagará R${:.2f} , por mês' .format(op, cores['vermelho'], vprod + ((vprod * 20) / 100), (vprod + ((vprod * 20) / 100) ) / 3))