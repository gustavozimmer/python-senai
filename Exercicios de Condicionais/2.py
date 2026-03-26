l1 = float(input("Digite um lado do triângulo: "))
l2 = float(input("Digite outro lado do triângulo: "))
l3 = float(input("Digite outro lado do triângulo: "))
if (l1 + l2 < l3 or l2 + l3 < l1 or l1 + l3 < l2):
    print("Erro a soma de 2 lados devem ser maior que o terceiro lado")
else:
    if (l1 == l2 != l3 or l2 == l3 != l1 or l3 == l1 != l2):
        print("O triangulo é Isósceles")
    elif (l1 != l2 and l2 != l3 and l3 != l1):
        print("O triângulo é escaleno")
    else:
        print("O triângulo é equilátero")
