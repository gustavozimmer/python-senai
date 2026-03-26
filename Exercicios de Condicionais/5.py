velocidade_carro = int(input("Velocidade do carro: "))
limite_via = int(input("Limite via: "))
if limite_via <= 100:
    tolerancia = limite_via + 7
else:
    tolerancia = limite_via * 1.07  

if velocidade_carro <= tolerancia:
    print("Isento")
elif velocidade_carro <= tolerancia* 1.20:
    print("Média")
elif (velocidade_carro > tolerancia * 1.2 and velocidade_carro <= tolerancia * 1.5):
    print("Grave")
else:
    print("Gravíssima + Suspensão")
