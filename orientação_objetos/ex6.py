class Aluno():
    def __init__(self, nome_aluno, curso, nota_final):
        self.nome_aluno = nome_aluno
        self.curso = curso
        self.nota_final = nota_final
    

    def status(self):
        print(f"Aluno: {self.nome_aluno} | Curso: {self.curso} | Situação: {"Reprovado" if self.nota_final < 7 else "Aprovado"}")
    