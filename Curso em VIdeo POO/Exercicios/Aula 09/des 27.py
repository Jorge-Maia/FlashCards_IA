from abc import ABC, abstractmethod
import random
from rich import print

class Personagem(ABC):
    def __init__(self, nome, vida,golpes=''):
        self.nome=nome
        self.vida=vida
        self.golpes=golpes

    def atacar(self,alvo,força):
        if self.vida>0:
            self.força=força
            dano=random.randint(1,força)
            self.alvo=alvo
            print(f'[green]{self.nome}({self.vida})[/] atacou [red]{self.alvo}({alvo.vida})[/] com o golpe [blue]{self.golpe()}[/] com uma força de {self.força}'
                  f'\n[blue]{self.alvo} recebeu um [red]dano de {dano}[/]!')
            alvo.receber(dano)
        else:
            print(f'Personagem morto!')
            return

    def receber(self,dano):
        self.vida-=dano
        if self.vida>0:
            print(f'{self.nome} ficou com {self.vida}!')
        else:
            print(f'{self} morreu com esse golpe!')
            return

    def __str__(self):
        return self.nome

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self,nome,vida):
        super().__init__(nome,vida)
        self.golpes = ['Golpe do machado', 'Golpe com as luvas', 'Chute']


    def curar(self):
        cura=random.randint(1,100)
        self.vida+=cura
        print(f'{self.nome} curou {cura} pontos de vida com sua atadura abençoada e ficou com {self.vida}!')

    def golpe(self):
        return random.choice(self.golpes)

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de fogo', 'Bola de gelo', 'Bloco de terra']

    def curar(self):
        cura = random.randint(1, 100)
        self.vida += cura
        print(f'{self.nome} curou {cura} pontos de vida com seu cajado mágico e ficou com {self.vida}!')

    def golpe(self):
        return random.choice(self.golpes)

p1=Guerreiro('Kratos', 2000)
p2=Mago('Merlin', 1000)

p1.atacar(p2,1000)
p2.atacar(p1,1000)
p2.curar()
p1.curar()
p1.atacar(p2,500)