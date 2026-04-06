frase = str(input("Digite uma frase: "))
a = e = i = o = u = 0
for letra in frase:
    if letra == "a":
        a += 1
    elif letra == "e":
        e += 1
    elif letra == "i":
        i += 1
    elif letra == "o":
        o += 1
    elif letra == "u":
        u += 1
print("QUANTIDADE DE VOGAIS NA FRASE:")
print(f"A: {a} E: {e} I: {i} O: {o} U: {u}")