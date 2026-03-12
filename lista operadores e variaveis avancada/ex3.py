preco = float(input("Informe o preço do produto: "))
frete = float(input("Digite o valor do frte: "))
quantidade = int(input("Digite a quantidade comprada: "))
valor_total = preco * quantidade + frete
print(f"O valor total da compra é {valor_total:.2f}")