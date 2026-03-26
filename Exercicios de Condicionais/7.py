import math
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

if a == 0:
    print("Não é uma equação do segundo grau")
else:
    discriminante = b**2 - 4*a*c

if discriminante < 0:
    print("A equação não possui raízes reais")
elif discriminante == 0:
    raiz1 = -b / 2 * a
    print(f"Raiz: {raiz1:.2f}")
else:
    raiz1 = (-b + math.sqrt(discriminante)) / 2 * a
    raiz2 = (-b - math.sqrt(discriminante)) / 2 * a
    print(f"Raiz 1: {raiz1:.2f}, Raiz 2: {raiz2:.2f}")

