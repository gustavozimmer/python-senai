def media(lista):
    media = sum(lista) / len(lista)
    return media

lista = []
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))

lista.append(n1)
lista.append(n2)
lista.append(n3)

print(media(lista))