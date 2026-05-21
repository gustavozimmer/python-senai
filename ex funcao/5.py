def eh_primo(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input("Digite um numero: "))
print(f"O numero {n} é primo: {eh_primo(n)}")