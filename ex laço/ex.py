import sys
usuario = "admin"
senha = "1234"
tentativa = 0
decisao = 0
produtos = []
while True:
    tentativa_usuario = str(input("Digite seu usuário: "))
    tentativa_senha = str(input("Digite sua senha: "))
    tentativa += 1
    if tentativa_senha == senha and tentativa_usuario == usuario:
        print("Bem vindo")
        break
    if tentativa == 3:
        print("Acesso negado")
        sys.exit()
    print(f"Tentativas restantes: {3 - tentativa}")

while True:
    print("""1. Cadastrar produto
2. Listar produtos
3. Atualizar estoque
4. Realizar venda
5. Relátorios
6. Sair
""")

    while True:
        decisao = input("Digite sua escolha: ")
        if decisao not in ('1','2', '3', '4', '5', '6'):
            print("Erro!")
        else:
            break
    
    if decisao == '1':
        while True:
            try:
                codigo = int(input("Digite o código: "))
                for produto in produtos:
                     if produto[0] == codigo:
                         raise ValueError
                if codigo < 0:
                    raise ValueError
                break
            except ValueError:
                print("Digite um numero positivo!")
        nome = str(input("Digite o nome do produto: "))
        while True: 
            try:
                preco = float(input("Digite "))
                if preco < 0:
                    raise ValueError
                break
            except ValueError:
                print("Digite um numero positivo!")
        while True:
            try:
                quantidade = int(input("Quantidade: "))        
                if quantidade < 0:
                    raise ValueError
                break
            except:
                print("Digite um numero inteiro positivo!")