try:
    valor = int(input("Digite um numero: "))
except ValueError as ve:
    print(f"Erro: {ve}")
