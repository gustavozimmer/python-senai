class Treinamento():
    def __init__(self, titulo, instrutor, duracao):
        self.titulo = titulo
        self.instrutor = instrutor
        self.duracao = duracao
    

    def descricao(self):
        print(f"Titulo: {self.titulo} | Instrutor: {self.instrutor} | Duração: {self.duracao} minutos")        
