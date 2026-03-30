numero1 = float(input("Digite um numero com casas decimais: "))
numero2 = float(input("Digite outro numero com casas decimais: "))
operacao = str(input("Digite a operação [+ - * /]: "))
if operacao == '+':
    total = numero1 + numero2
elif operacao == '-':
    total = numero1 - numero2
elif operacao == '*':
    total = numero1 * numero2 
elif operacao == '/':
    total = numero1 / numero2
print(f"Total: {total}")