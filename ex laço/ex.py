from collections import Counter
# import sys
# usuario = "admin"
# senha = "1234"
# tentativa = 0
# decisao = 0
produtos = []
historico_produto = []
historico_qtd = []
historico_valor = []
zero = False
# while True:
#     tentativa_usuario = str(input("Digite seu usuário: "))
#     tentativa_senha = str(input("Digite sua senha: "))
#     tentativa += 1
#     if tentativa_senha == senha and tentativa_usuario == usuario:
#         print("Bem vindo")
#         break
#     if tentativa == 3:
#         print("Acesso negado")
#         sys.exit()
#     print(f"Tentativas restantes: {3 - tentativa}")

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
                preco = float(input("Digite o preço: "))
                if preco < 0:
                    raise ValueError
                break
            except ValueError:
                print("Digite um numero positivo!")
        while True:
            try:
                estoque = int(input("Quantidade: "))        
                if estoque < 0:
                    raise ValueError
                break
            except:
                print("Digite um numero inteiro positivo!")
        tipo_produto = [codigo, nome, preco, estoque]
        produtos.append(tipo_produto)
    if decisao == "2":
        if not produtos:
            print("Nenhum produto adicionado")
        else:
            print()
            for produto in produtos:
                print(f"{produto[0]} | {produto[1]} | {produto[2]} | {produto[3]}")
            print()
    if decisao == "3":
        print("""1. Adicionar estoque
2. Remover estoque""")
        while True:
            if not produtos:
                print("Nenhum produto adicionado")
                zero = True
                break
            escolha_estoque = input("Digite sua escolha: ")
            if escolha_estoque not in ('1', '2'):
                print("Escolha 1 ou 2")
            else:
                print()
                for produto in produtos:
                    print(f"{produto[0]} | {produto[1]} | {produto[2]} | {produto[3]}")
                print()
                break
        if zero:
            print()
            continue
        zero = False
        while True:
                try:
                    indice = -1
                    codigo_pesquisa = int(input("Digite o codigo do produto desejado: "))
                    if codigo_pesquisa < 0:
                        raise ValueError
                    for produto in produtos:
                        if produto[0] != codigo_pesquisa:    
                            continue
                        else:
                            indice = produtos.index(produto)
                            break
                    if indice >= 0:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Digite um número válido")
        if escolha_estoque == "1":
            while True: 
                try:
                    adicao = int(input("Adicione ao estoque: "))
                    if adicao < 0:
                        raise ValueError
                except ValueError:
                    print("Digite um numero positivo")
                break
            produtos[indice][3] += adicao
            print("Produto adicionado com sucesso!")
        
        if escolha_estoque == "2":
            while True: 
                try:
                    remocao = int(input("Remova do estoque: "))
                    if remocao < 0 or remocao > produtos[indice][3]:
                        raise ValueError
                    break
                except ValueError:
                    print("Digite um numero menor ou igual a quantidade do estoque")
            produtos[indice][3] -= remocao
            print("Produto removido com sucesso")          
    
    if decisao == '4':
        while True:
            if not produtos:
                print("Nenhum produto adicionado")
                break
            else:
                print()
                for produto in produtos:
                    print(f"{produto[0]} | {produto[1]} | {produto[2]} | {produto[3]}")
                print()
                break
        while True:
                try:
                    codigo_pesquisa = int(input("Digite o codigo do produto desejado: "))
                    if codigo_pesquisa < 0:
                        raise ValueError
                    for produto in produtos:
                        if produto[0] != codigo_pesquisa:    
                            raise ValueError
                        else:
                            indice = produtos.index(produto)
                            break
                    break
                except ValueError:
                    print("Digite um produto válido")
        while True: 
            try:
                remocao = int(input("Remova do estoque: "))
                if remocao < 0 or remocao > produtos[indice][3]:
                    raise ValueError
                break
            except ValueError:
                    print("Digite um numero menor ou igual a quantidade do estoque")
        produtos[indice][3] -= remocao
        preço_total = remocao * produtos[indice][2]
        historico_produto.append(produtos[indice][1])
        historico_qtd.append(remocao)
        historico_valor.append(preço_total)
        print(historico_produto, historico_qtd, historico_valor)

    if decisao == '5':
        print("""1. Total vendido
2. Produto mais vendido
3. Produto com maior estoque
4. Listar vendas
""")
        
        while True:
            escolha_relatorio = input("Digite sua escolha: ")
            if escolha_relatorio not in ('1','2', '3', '4'):
                print("Digite um numero de 1 a 4")
            else:
                break
        soma_total = 0
        if escolha_relatorio == '1':
            for preco in historico_valor:
                soma_total += preco
            print(f"O total vendido é: {soma_total}") 
        elif escolha_relatorio == '2':
            contador = Counter(historico_produto)
            mais_vendido = contador.most_common(1)
            print(f"O produto mais vendido é {mais_vendido[0][0]}")
        elif escolha_relatorio == '3':
            maior_estoque = produtos[0][3]
            for produto in produtos:
                if produto[3] > maior_estoque:
                    maior_estoque = produto[3]
                    nome = produto[1]
            print(f"O produto com maior estoque é {nome}")
        elif escolha_relatorio == '4':
            print('-' * 10 + "Lista de vendas"  + '-' * 10)