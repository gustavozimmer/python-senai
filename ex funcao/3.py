def converter_celsius_para_fahrenheit(c):
    f = c * 1.8 + 32
    return f

c = float(input("Digite o valor a ser convertido em C°: "))
print(f"C°: {c} F°: {converter_celsius_para_fahrenheit(c):.2f}")