def fatorial(numero):
    fatorial = 1
    for c in range(1, numero + 1):
        fatorial *= c
    return fatorial
print(fatorial(9))