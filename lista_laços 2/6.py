fatorial = 1
while True:
    n = int(input("Digite um numero: "))
    if n < 0:
        print("Erro! Digite um numero positivo")
    else:
        for c in range (n, 1, -1):
            fatorial *= c
            print(fatorial)
        decisao = str(input("Deseja continuar [s/n]: ")).strip().lower()
        if decisao == 'n':
            break
        fatorial = 1
print("Obrigado volte sempre")
