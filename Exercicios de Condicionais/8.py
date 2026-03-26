saque = int(input("Digite o valor a ser sacado: "))
nota_100 = nota_50 = nota_20 = nota_10 = nota_5 = nota_2 = 0
if saque == 0:
    print("O saque deve ser maior que 0")
elif (saque % 2 != 0 and saque % 5 != 0):
    print("Valor impossível de ser sacado com as notas disponíveis")
else:
    nota_100 = saque // 100
    saque -= nota_100 * 100
    if saque > 0:
        nota_50 = saque // 50
        saque -= nota_50 * 50
    if saque > 0:
        nota_20 = saque // 20
        saque -= nota_20 * 20
    if saque > 0:
        nota_10 = saque // 10
        saque -= nota_10 * 10
    if saque > 0:
        nota_5 = saque // 5
        saque -= nota_5 * 5
    if saque > 0:
        nota_2 = saque // 2
        saque -= nota_2 * 2
    print(f"100: {nota_100} | 50: {nota_50} | 20: {nota_20} | 10: {nota_10} | 5: {nota_5} | 2: {nota_2}   ")
