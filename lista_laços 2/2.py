maior = num = int(input("Digite um numero inteiro: "))
contador = 0

while num != 1:
    if num % 2 == 0:
        num /= 2
    else:   
        num = num * 3 + 1
    if num > maior:
        maior = num
    contador += 1
    print(num)
print(f"A quantidade de iterações necessarias: {contador}")
print(f"O maior numero foi: {maior}")