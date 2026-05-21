def contagem_regressiva(n):
    print(n)
    n -= 1
    if n >= 1:
        contagem_regressiva(n)

n = int(input("Digite um numero: "))
print("Contagem regressiva:")
contagem_regressiva(n)
print("fim")
