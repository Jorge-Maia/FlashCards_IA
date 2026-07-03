from principal import Aluno, Funcionario, Professor,Pessoa
from rich import inspect

a1=Aluno("Jorge", 17, 'Informatica', 't20' )
a1.fazer_aniversario()
a1.fazer_matricula()
#inspect(a1,methods=True)

p1=Professor('Marcos',30,'Biologia', 'Mestrado')
p1.dar_aula()
#inspect(p1,methods=True)

f1=Funcionario('Maria',49, 'Secretária', 'Secretaria')
f1.bater_ponto()
#inspect(f1,methods=True)

a1.estudar()
p1.estudar()
f1.estudar()