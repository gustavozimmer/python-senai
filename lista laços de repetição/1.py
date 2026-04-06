contador = 0
for c in range (1, 11):
    n = int(input("Digite um numero: "))
    if n % 3 == 0:
        contador += 1
print(f"{contador} numeros são multiplos de 3")