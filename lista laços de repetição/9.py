qtde_numero = int(input("Digite quantos numeros deseja digitar: "))
lista_numeros = []
soma = 0
for c in range(0, qtde_numero):
    numero = int(input("Digite um numero: "))
    lista_numeros.append(numero)
    soma += numero
media = soma / len(lista_numeros)
print(f"A média é {media}")
print("Abaixo da média")
for c in lista_numeros:
    if c < media:
        print(c)