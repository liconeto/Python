texto = ' Desafio 026 '
print(' {:*^30}'. format(texto))
frase = str(input('Digite uma frase : ')).upper().strip()
A = frase.count('A')
print('A frase digitada oi : {}' .format(frase))
print('Quantas vezes a letra a aparece na frase? : {}' .format(A))
print('Em qual posição ela aparece a primeira vez ? : {}' .format(frase.find('A')+1))
print('Em qual posição ela aparece a primeira vez ? : {}' .format(frase.rfind('A')+1))