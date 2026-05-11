try:
    num = int(input("Digite um numero: "))
    resultado = 10 / num
    print(f"Resultado {resultado}")
except ZeroDivisionError:
    print("Não é possivel dividir por zero")
except ValueError:
    print("Você não digitou um numero")