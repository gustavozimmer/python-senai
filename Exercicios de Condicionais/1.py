import math
GRAVIDADE = -9.8
h0 = float(input("Digite a altura em metros: "))
if h0 < 0:
    print("Altura inválida: a altura não pode ser negativa")
else:
    t = math.sqrt((h0 * -2) / GRAVIDADE)
    print(f"A quantidade de tempo da queda é {t:.2f}")
    