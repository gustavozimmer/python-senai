senha = "Senha123"

qtde_tentativa = 0
while qtde_tentativa < 3:
    tentativa = str(input("Digite sua senha: "))
    qtde_tentativa += 1
    if tentativa == senha:
        print(f"Bem vindo! tentativas de acesso: {qtde_tentativa}")
        break
    print("Erro! tente novamente")
if qtde_tentativa == 3:
    print("Acesso bloqueado")
    