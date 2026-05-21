matriz = [[],[],[]]
soma = 0
soma_diag_principal = 0
qtde_pares = 0
maior = 0
for i in range (0, 3):
    for j in range (0, 3):
        n = int(input(f"Digite o valor da posição {i}x{j}: "))
        if i == j:
            soma_diag_principal += n
        if n % 2 == 0:
            qtde_pares += 1
        soma += n
        matriz[i].append(n)
        if n > maior:
            maior = n
print(f"Soma de todos os elementos: {soma}")
print(f"Maior valor: {maior}")
print(f"Soma diagonal principal: {soma_diag_principal}")
print(f"Existem {qtde_pares} numeros pares")
