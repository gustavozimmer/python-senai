class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def detalhes(self):
        print(f"Marca: {self.marca}  Modelo: {self.modelo}  ano: {self.ano}")


carro1 = Carro("honda", "civic", 2008)
carro1.detalhes()
