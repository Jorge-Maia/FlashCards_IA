from abc import ABC,abstractmethod

class BebidaQuente(ABC):
    def preparar(self):
        print(f'--- Iniciando o Preparo ---')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print(f'--- Finalizando o Preparo ---')

    def ferver_agua(self):
        print(f'1-Fervendo água a 100°C...')

    @abstractmethod

    def misturar(self):
        pass

    @abstractmethod

    def servir(self):
        pass

class Cafe(BebidaQuente):

    def misturar(self):
        print (f'2- Passando água pressurizada pelo pó de café moído...')

    def servir(self):
        print(f'3- Servindo em xícara pequena.')

class Cha(BebidaQuente):

    def misturar(self):
        print(f'2- Mergulhando o sachê de ervas na água...')

    def servir(self):
        print(f'3-Servindo na caneca de porcelana com limão')



bebida = Cha()
bebida.preparar()
