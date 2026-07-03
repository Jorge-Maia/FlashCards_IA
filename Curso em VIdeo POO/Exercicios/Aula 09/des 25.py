from abc import ABC,abstractmethod
from rich.table import Table
from rich import print

class Transporte(ABC):
    def __init__(self,km=0):
        self.km = km

    @abstractmethod

    def calcular(self):
        pass

class Moto(Transporte):
    def __init__(self, km):
        super().__init__(km)

    def calcular(self):
        calcular = self.km*0.5
        return f' R${calcular:.2f}'

class Caminhão(Transporte):
    def __init__(self,km):
        super().__init__(km)

    def calcular(self):
        if self.km>50:
            calcular = self.km*1.20
            return f'R${calcular:.2f}'
        else:
            return f'Menor que 50Km!'

class Drone(Transporte):
    def __init__(self,km):
        super().__init__(km)

    def calcular(self):
        if self.km<10:
            calcular = self.km*9.5
            return f'R${calcular:.2f}'
        else:
            return f'Maior do que o limite de 10Km!'

dist=60
a=Caminhão(dist)
print(a.calcular())

m=Moto(dist)
c=Caminhão(dist)
d=Drone(dist)

tabela=Table(title='Tabela de fretes')
tabela.add_column('Distância',justify='center')
tabela.add_column('Tipo',justify='center')
tabela.add_column('Frete',justify='center')

tabela.add_row(f'{dist}Km','Moto', f'{m.calcular()}Km')
tabela.add_row(f'{dist}Km','Drone', f'{d.calcular()}')
tabela.add_row(f'{dist}Km','Caminhão', f'{c.calcular()}')

print(tabela)
