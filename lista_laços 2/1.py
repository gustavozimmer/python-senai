n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
contador = 0
if (n1 < n2):
    for c in range(n1, n2 + 1):
        if c < 2:
            continue
        primo = True
        for i in range(2, int(c**0.5) + 1):
            if c % i == 0:
                primo = False
                break 
        if primo:
            print(c)
            contador += 1
    print(f"A quantidade final de numeros primos encontrados foram: {contador}")
else:
    print("O inicio deve ser maior que o final")
