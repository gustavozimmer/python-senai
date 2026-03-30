horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

if horas > 24 or horas < 0:
    print("Inválido")
elif minutos > 59 or minutos < 0:
    print("Inválido")
elif segundos > 59 or segundos < 0:
    print("Inválido")
else:
    print("Hora válida")