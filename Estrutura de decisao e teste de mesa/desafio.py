from random import randint

aleatorio = randint(1, 10)

palpite1 = int(input("Tente advinhar o numero: "))
if palpite1 == aleatorio:
    print("Voce acertou, parabens!")
else:
    palpite2 = int(input("Tente novamente: "))
    if palpite2 == aleatorio:
        print("Voce acertou, parabens!")
    else:
        print(f"Você perdeu o numero era {aleatorio}")