from random import choice
cara = 0
while cara < 3:
    sorteio = choice(["cara", "coroa"])
    print(sorteio)
    if sorteio == "cara":
        cara += 1
    else:
        cara = 0