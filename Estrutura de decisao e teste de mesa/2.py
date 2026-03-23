peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / altura**2

if imc < 18.5:
    classificacao = "Baixo Peso"
elif imc <= 24.9:
    classificacao = "Normal"
elif imc <= 29.9:
    classificacao = "Sobrepeso" 
elif imc <= 34.9:
    classificacao = "Obesidade"
else:
    classificacao = "Obesidade Mórbida"
print(f"Seu imc é {imc:.2f}, classificação: {classificacao}")