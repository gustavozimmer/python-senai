lado1 = float(input("Digite o valor do lado 1: "))
lado2 = float(input("Digite o valor do lado 2: "))
lado3 = float(input("Digite o valor do lado 3: "))
lado4 = float(input("Digite o valor do lado 4: "))

if lado1 == lado2 == lado3 == lado4:
    print("Quadrado")
elif lado1 == lado2 and lado3 == lado4:
    print("Retangulo")
elif lado2 == lado3 and lado1 == lado4:
    print("Retangulo")
elif lado3 == lado1 and lado2 == lado4:
    print("Retangulo")
else:
    print("Quadrilatero qualquer")

