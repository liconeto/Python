texto = ' Desafio 036 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

print('\033[1;31mBanco Curso em Vídeo \033[m')
imovel = float(input('Informa o valor do Imovel R$: '))
salario = float(input('Informe o seu salario R$: '))
tempo = int(input('Informe em quantos ano você vai pagar :'))

prestacao = imovel / (tempo * 12)
compro = (prestacao * 100) / salario
if prestacao > (salario * 0.30):
    print('Emprestimo {}REPROVADO!{} \n'
          'Por quê a prestação vai comprometer mais de 30% do seu salário \n'
          'Seu salário {}{:.2f}{}, sua prestação {}{:.2f}{}, \n tempo de pagamento {}{}{} anos \n  Valor comprometido do salário {}{:.2f}%{} ' .format(
        cores['vermelho'], limpa, cores['amarelo'], salario, limpa, cores['vermelho'], prestacao, limpa, cores['ciano'], tempo, limpa, cores['vermelho'], compro, limpa))
else:
    print('Emprestimo {}APROVADO!{} \n'
          'Valor do imóvel R${}{}{} \n Seu salário R${}{}{} \n Pagamento em {}{}{}anos'
          '\n Valor comprometido do salário {}R${:.2f}, {:.2f}%{}'
          ''.format(cores['azul'], limpa, cores['ciano'], imovel, limpa, cores['verde'], salario, limpa, cores['roxo'], tempo, limpa, cores['vermelho'], prestacao, compro, limpa))