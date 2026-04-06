n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
contador = 0
for c in range(n1, n2 + 1):
    contador = 0
    for i in range(1, n2 + 1):
        if c % i == 0:
            contador += 1
    if contador <= 2 and c != 1:
        print(c)