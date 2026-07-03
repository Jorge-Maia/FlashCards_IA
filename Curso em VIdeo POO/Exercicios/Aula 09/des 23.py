import math
from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self,l):
        self.l=l

    @abstractmethod

    def area(self):
        pass

    def perimetro(self):
        pass

class Quadrado(Poligono):

    def __init__(self,l):
        super().__init__(l)

    def area(self):
        area=self.l*self.l
        return f'A área do quadrado é {area:.2f}'

    def perimetro(self):
        perimetro=self.l*4
        return f'O perímetro é {perimetro:.2f}'

class Circulo(Poligono):
    def __init__(self,l):
        super().__init__(l)

    def area(self):
        area=self.l*self.l*math.pi
        return f'A área do círculo de raio {self.l} é igual a {area:.1f}'

    def perimetro(self):
        perimetro=self.l*math.pi*2
        return f'O perímetro é {perimetro:.1f}'





p1=Circulo(20)
print(p1.area())
print(p1.perimetro())