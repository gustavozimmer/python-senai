denominador = 2
contador = 1
soma = 1
while True:
    numero = 1 / denominador
    denominador += 1
    if numero < 0.001:
        break
    soma += numero
    contador += 1
print(soma, contador) 