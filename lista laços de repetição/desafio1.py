taxa_reproducao = int(input("Digite a taxa de reprodução (%): "))
taxa_mortalidade = int(input("Digite a taxa de mortalidade (%): "))
numero_inicial = int(input("Digite o número inicial de coelhos: "))
numero_geracoes = int(input("Digite a quantidade de gerações: "))

if numero_inicial < 2:
    print("Caso impossível: População insuficiente para reprodução.")
else:
    for c in range(0, numero_geracoes):
        nascimentos = numero_inicial * (taxa_reproducao / 100)
        mortes = numero_inicial * (taxa_mortalidade / 100)
        numero_inicial += int(nascimentos - mortes)

    print(f"População final após {numero_geracoes} gerações: {numero_inicial}")