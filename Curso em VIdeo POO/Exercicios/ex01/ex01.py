#Declaração de Classe
class Gafanhoto:
    def __init__(self):  #método construtor
    #Atributos de Instancia
        self.nome=""
        self.idade=0
        self.aniversário=""

    #Métodos de Instância
    def aniversario(self):
        self.idade=self.idade+1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos'

#Declaração de Objetos
g1=Gafanhoto()
g1.nome=input('Qual seu nome? ')
g1.idade=int(input('Quantos anos vc tem? ' ))
g1.aniversário=input('Você fez aniversário? [S/N] ').upper()
if g1.aniversário=='S':
    g1.aniversario()
print(g1.mensagem())

g2=Gafanhoto()
g2.nome="Joao"
g2.idade=int(input('Quantos anos vc tem?' ))
print(g2.mensagem())