import math
x_c = float(input("Digite a coordenada x do centro do círculo: "))
y_c = float(input("Digite a coordenada y do centro do círculo: "))
raio = float(input("Digite o raio do círculo: "))
x_p = float(input("Digite a coordenada x do ponto P: "))
y_p = float(input("Digite a coordenada y do ponto P: "))
distancia = math.sqrt((x_p - x_c)**2 + (y_p - y_c)**2)
print(f"Distância calculada: {distancia:.2f}")
if distancia < raio:
    print("O ponto está: DENTRO")
elif distancia == raio:
    print("O ponto está: NA BORDA")
else:
    print("O ponto está: FORA")