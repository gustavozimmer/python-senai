from ex1 import Carro
from ex2 import Pessoa
from ex3 import Manual
from ex4 import Produto
from ex5 import Treinamento
from ex6 import Aluno

carro1 = Carro("Honda", "Civic", "2025")
carro2 = Carro("Toyota", "Supra", "2007")

pessoa1 = Pessoa("Gustavo", 20, "Vendas")
pessoa2 = Pessoa("João", 21, "Compras")
pessoa3 = Pessoa("Pedro", 40, "Recursos Humanos")

manual1 = Manual("Fundamentos de Java", "Helio", 2015)
manual2 = Manual("Fundamentos de SQL", "Castro", 2016)

produto1 = Produto("Pneu", 200, 10)
produto2 = Produto("Volante", 100, 15)
produto3 = Produto("Suspensão", 300, 20)

treinamento1 = Treinamento("Boas praticas na progamação", "João", 60)
treinamento2 = Treinamento("Trabalho em grupo", "Roberta", 180)

aluno1 = Aluno("Joana", "Matemática", 4)
aluno2 = Aluno("Nathalia", "Design", 9)
aluno3 = Aluno("Vania", "Costura", 10)

carro1.detalhes()
carro2.detalhes()

pessoa1.apresentar()
pessoa2.apresentar()
pessoa3.apresentar()

manual1.informacoes()
manual2.informacoes()

produto1.mostrar_estoque()
produto2.mostrar_estoque()
produto3.mostrar_estoque()

treinamento1.descricao()
treinamento2.descricao()

aluno1.status()
aluno2.status()
aluno3.status()
