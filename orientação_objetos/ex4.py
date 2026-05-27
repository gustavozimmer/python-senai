class Produto():
    def __init__(self, nome_produto, preco_unitario, quantidade_disponivel):
        self.nome_produto = nome_produto
        self.preco_unitario = preco_unitario
        self.quantidade_disponivel = quantidade_disponivel
    


    def mostrar_estoque(self):
        print(f"Produto: {self.nome_produto} | Preço: R${self.preco_unitario} | Quantidade em estoque: {self.quantidade_disponivel}")


        