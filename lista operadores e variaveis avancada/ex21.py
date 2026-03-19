import math
lado1 = float(input("Digite o lado 1: "))
lado2 = float(input("Digite o lado 2: "))
lado3 = float(input("Digite o lado 3: "))
semiperimetro = (lado1 + lado2 + lado3) / 2
area = math.sqrt(semiperimetro* (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3))
print(f"O trinangulo é isóceles {lado1 == lado2 or lado2 == lado3 or lado3 == lado1}")
print(f"O trinangulo é equilatero {lado1 == lado2 == lado3}")
print(f"O trinangulo é escaleno {lado1 != lado2 and lado2 != lado3 and lado3 != lado1}")
print(f"A área utilizando a formula de heron é: {area:.2f}")
