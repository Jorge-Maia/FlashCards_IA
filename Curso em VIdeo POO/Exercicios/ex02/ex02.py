#Declaração de Classe
class Gafanhoto:
    def __init__(self,nome='',idade=0):  #método construtor
    #Atributos de Instancia
        self.nome=nome
        self.idade=idade
        self.aniversário=""

    #Métodos de Instância
    def aniversario(self):
        self.idade=self.idade+1

    def __str__(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos'

    def __getstate__(self):
        return f"Estado: nome={self.nome}, idade={self.idade}"

#Declaração de Objetos
g1=Gafanhoto('Maria',17)
g1.aniversario()
print(g1)

g2=Gafanhoto('Claudio',25)
g2.aniversario()
print(g2)

print(g1.__dict__)
print(g2.__getstate__())   #PERSONALIZA COMO APARECER OS VALORES
print(g1.__class__)