qtde_numero = int(input("Digite a quantidade de numeros que quer digitar: "))
lista_numeros = []
for c in range(0, qtde_numero):
    n = int(input("Digite um numero: "))
    lista_numeros.append(n)
lista_numeros.sort()
segundo_maior = lista_numeros[len(lista_numeros) - 2]
print(f"O segundo maior numero é {segundo_maior}")
