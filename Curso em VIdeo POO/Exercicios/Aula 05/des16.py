class Funcionario:
    def __init__(self,nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        print(f'Meu nome é {self.nome}! Estou no setor {self.setor} trabalhando no cargo de {self.cargo}!')

c1=Funcionario('Jorge', 'TI', 'Auxiliar de TI')
c1.apresentar()
c2=Funcionario('Gi', 'Engenharia', 'Auxiliar de Edificações')
c2.apresentar()