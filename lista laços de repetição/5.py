senha = "Senha123"
tentativas = 0
while True:
    senha_usuario = str(input("Digite sua senha: "))
    if senha != senha_usuario:
        print("Senha inválida")
        tentativas += 1
        if tentativas >= 3:
            print("BLOQUEADO")
            break    
        
    else:
        print("Acesso permitido")
        