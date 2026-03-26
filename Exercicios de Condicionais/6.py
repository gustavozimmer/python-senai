dia = int(input("Digite o dia de nascimento: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 ):
    dia_max = 31
elif (mes == 2):
    if (ano % 100 == 0 and ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        dia_max = 29
    else:
        dia_max = 28
else:
    dia_max = 30

if (dia <= dia_max and mes <= 12 and ano >= 1900 and ano <= 2026):
    print("A data é válida")
else:
    print("Data inválida")
       
