class Pessoa:
    def __init__(self,nome='',idade=''):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

class Aluno(Pessoa):
    def __init__(self,nome,idade, curso, turma):
        super().__init__(nome,idade)
        self.curso = curso
        self.turma=turma

    def fazer_matricula(self):
        print(f'{self.nome} acabou de fazer matricula!')


class Professor(Pessoa):
    def __init__(self,nome,idade,especialidade,nivel):
        super().__init__(nome,idade)
        self.especialidade=especialidade
        self.nivel=nivel
        print(f'Professor {self.nome} começou a dar aula!')

    def dar_aula(self):
        pass

class Funcionario(Pessoa):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo=cargo
        self.setor=setor

    def bater_ponto(self):
        print(f'Funcionario {self.nome} acabou de bater ponto!')