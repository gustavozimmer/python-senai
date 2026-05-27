class Pessoa():
    def __init__(self, nome, idade, setor):
        self.nome = nome
        self.idade = idade
        self.setor = setor


    def apresentar(self):
        print(f"Colaborador {self.nome} tem {self.idade} anos de idade e trabalha no setor: {self.setor}")        
