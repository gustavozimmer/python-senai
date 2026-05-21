try:
    print(10 / 0)
except ZeroDivisionError:
    print("Não dá para dividir por zero")
finally:
    print("Esse bloco será executado de qualquer forma")