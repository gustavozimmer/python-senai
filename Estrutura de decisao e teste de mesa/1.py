ano = int(input("Digite o ano desejado: "))
if (ano % 100 == 0 and ano % 400 == 0):
    print(ano, "É bissexto")
elif (ano % 4 == 0 and ano % 100 != 0):
    print(ano, "É bissexto")
else:
    print("Não é bissexto")
