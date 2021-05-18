def someAte(limite):
    """Retorna a soma de 1 + 2 + 3 ... n """

    soma = 0
    numero = 1
    while numero <= limite:
        soma = soma + numero
        numero = numero + 1
    return soma
print(someAte(4))

print(someAte(1000))
