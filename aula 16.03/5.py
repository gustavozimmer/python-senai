usuario = {"nome": "Carlos", "email": "carlos@gmail.com"}
try:
    contato = usuario["telefone"]
except KeyError:
    try:
        print("Telefone não encontrado. Tentando email...")
        contato = usuario["email"]
        print(f"Contato definido como e-mail: {contato}")
    except KeyError:
        print("Nenhuma forma de contato cadastrada")