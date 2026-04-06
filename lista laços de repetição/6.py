lista_pares = []
lista_impares = []
for c in range (1, 11):
    n = int(input("Digite um numero: "))
    if n % 2 == 0 and n != 0:
        lista_pares.append(n)
    
    elif n % 2 != 0 and n != 0:
        lista_impares.append(n)
print("lista pares", lista_pares)
print("lista impares", lista_impares)