from random import randint

numero = randint(1, 100)
qtde_tentativas = 1
while qtde_tentativas < 10:
    qtde_tentativas += 1
    tentativa = int(input("Digite um numero: "))
    diferença = tentativa - numero
    if diferença == 0:
        print("Você acertou!")
        break
    elif diferença > 20:
        print("Muito alto")
    elif diferença > 10:
        print("Alto")
    elif diferença > 0:
        print("Pouco alto")
    elif diferença > -10:
        print("baixo")
    else:
        print("Muito baixo")
    if qtde_tentativas == 10:
        print("Voce perdeu")