def maior_n(lista):
    maior = 0
    for c in lista:
        if c > maior:
            maior = c
    return maior

qtde = int(input("Quantos numeros deseja digitar: "))
lista = []
for c in range(qtde):
    n = int(input("Digite um numero: "))
    lista.append(n)

print(f"O maior numero é {maior_n(lista)}")
