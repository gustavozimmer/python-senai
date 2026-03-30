saque = int(input("Digite o valor a ser sacado: "))
lista_cedulas = [100, 50, 20, 10, 5, 2]
lista_qtde_cedulas = []
for cedula in lista_cedulas:
    qtde_cedulas = saque // cedula
    saque %= cedula
    lista_qtde_cedulas.append(qtde_cedulas)
if saque > 0:
    print('erro!')
else:
    for c in range(len(lista_qtde_cedulas)):
        print(f"{lista_cedulas[c]}: quantidade {lista_qtde_cedulas[c]}")

