def imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))
print(f"Seu imc é {imc(peso, altura):.2f}")
