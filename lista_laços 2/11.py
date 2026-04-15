n = int(input("Digite um número inteiro: "))
primos = []
for i in range(n + 1):
    primos.append(True)
primos[0] = False
primos[1] = False
for p in range(2, n + 1):
    if primos[p] == True:
        for multiplo in range(p * 2, n + 1, p):
            primos[multiplo] = False
lista_final = []
quantidade = 0
for i in range(2, n + 1):
    if primos[i] == True:
        lista_final.append(i)
        quantidade = quantidade + 1

print("Lista de primos:", lista_final)
print("Quantidade total:", quantidade)