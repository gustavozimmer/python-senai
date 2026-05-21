try:
    x = int(input("Enter a number: "))
    x = x + 10
    print(x)
except ValueError:
    print("A resposta deve ser um numero")
    