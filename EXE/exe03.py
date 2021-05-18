
horaAtual = input("Informe a hora atual!\n")
horaAlarme = input("Informe a hora do alarme\n")
dia = 24
horaAtual = int(horaAtual)
horaAlarme = int(horaAlarme)

print(horaAtual)
print(horaAlarme)

despertar = horaAtual + horaAlarme

print("O alarme vai desperatar em "+str(int(despertar / dia))+" dias e "+str(despertar % dia)+" horas")

