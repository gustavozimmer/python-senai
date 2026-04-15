while True:
    print("""[1] Multiplicar
[2] Dividir
[3] Sair""")
    escolha = int(input("Digite sua escolha: "))
    if escolha == 3:
        break
    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite outro numero: "))
    if escolha == 1:
        resultado = numero1 * numero2
    else: 
        resultado = numero1 / numero2
    print(f"O resultado é {resultado}")
print("Obrigado, volte sempre :)")
