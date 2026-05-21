numero = int(input("Digite um numero: "))
divisores = []

for c in range(1, numero):
    if numero % c == 0:
        divisores.append(c)

soma = 0

for numeros in divisores:
    soma += numeros

if soma == numero:
    print("O número é perfeito")
else:
    print("O número não é perfeito")
    