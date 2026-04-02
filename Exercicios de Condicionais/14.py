numero = int(input("Digite um número inteiro de exatamente 5 dígitos: "))
if numero < 10000 or numero > 99999:
    print("Erro: O número deve possuir exatamente 5 dígitos.")
else:
    original = numero
    d1 = numero // 10000
    d2 = (numero // 1000) % 10
    d4 = (numero // 10) % 10
    d5 = numero % 10
    if d1 == d5 and d2 == d4:
        print(f"O número {original} é um palíndromo.")
    else:
        print(f"O número {original} NÃO é um palíndromo.")