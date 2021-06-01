from datetime import date
import emoji
texto = ' Desafio 039 '
print(' {:*^30}'. format(texto))

limpa = '\033[m'
cores = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
         'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}

print('{}{} Alistamento {}militar {}curso em {}vídeo {}'. format(cores['verde'], emoji.emojize(":Brazil:"), cores['amarelo'], cores['verde'],
                                                            cores['amarelo'], limpa))
idade = int(input('Informe o seu ano de nascimento :'))
ano = date.today().year
tempo = ano - idade
if tempo <= 16:
    print('{}{} Você tem apenas {} aguarde para se alistar no serviço militar!{}' .format(cores['amarelo'], emoji.emojize(' :warning:'),tempo, emoji.emojize(' :warning:')))
elif tempo == 17 or tempo == 18:
    print('{}{} Você tem {}. É hora de se alistar no serviço militar! {}' .format(cores['verde'], emoji.emojize(' :fireworks:'),tempo, emoji.emojize(' :fireworks:')))
else:
    print('{} {} Você tem {} .Já passou da hora de se alistar! {}' .format(cores['vermelho'], emoji.emojize(":SOS_button:"), tempo, emoji.emojize(":SOS_button:")))
