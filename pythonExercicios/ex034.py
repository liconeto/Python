texto = ' Desafio 034'
print(' {:*^30}'. format(texto))

print('Informe seu salário para ser calculado o aumento !')
salario = float(input('Salário : '))

if salario > 1250.00:
    print('Seu salário é : R${} \nCom o aumento será R${:.2f}'
          .format(salario, salario + (salario * 0.10)))
else:
    print('Seu salário é R${} \nCom o aumento será : R${:.2f}'
          .format(salario, salario + (salario * 0.15)))
