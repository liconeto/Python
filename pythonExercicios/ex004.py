texto = ' Desafio 004 '
print('\033[1;34m {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}
algo = input('{}Digite algo: {}' .format(cores['vermelho'], limpa))
print('{}O valor digitado foi {}{}' .format(cores['azul'], algo, limpa))
print('{}O valor é do tipo {}{}' .format(cores['roxo'],type(algo), limpa))
print('{}É espaço ?: {}{}' .format(cores['amarelo'],algo.isspace(), limpa))
print('{}É númeco ?: {}{}' .format(cores['ciano'], algo.isnumeric(), limpa))
print('{}É alfabético ?: {}{}' .format(cores['cinza'], algo.isalpha(), limpa ))
print('{}É alfanúmerico ?: {}{}' .format(cores['vermelho'], algo.isalnum(), limpa))
print('{}Está em maiúscula ?: {}{}' .format(cores['verde'], algo.isupper(), limpa))
print('Está em minuscula ?: {}' .format(algo.islower()))
print('Está capitalizada ?: {}' .format(algo.istitle()))
