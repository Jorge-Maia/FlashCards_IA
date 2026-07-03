from abc import ABC,abstractmethod
from rich import inspect
from rich.panel import Panel
from rich import print

class Funcionario(ABC):
    salmin=1_612
    inss=7.5

    def __init__(self,nome=None):
        self.nome=nome
        self.salario_bruto=0
        self.salario=0

    @abstractmethod
    def calcular(self):
        pass

    def analisar(self):
        base=self.salario/self.salmin
        painel=Panel(f'O salário de [blue]{self.nome}[/] ({self.__class__.__name__}) é de [green]R${self.salario:.2f}[/] e correspode a [yellow]{base:.1f} salários mínimos[/]',title='Funcionario')
        print(painel)

class Horista(Funcionario):

    def __init__(self,nome,valor_hora=7.5,hora=220):
        super().__init__(nome)
        self.valor_hora=valor_hora
        self.hora=hora
        self.salario_bruto=valor_hora*hora

    def calcular(self):
        self.salario=self.salario_bruto-(self.salario_bruto*self.inss/100)

class Mensalista(Funcionario):
    def __init__(self,nome,salariobruto=Funcionario.salmin):
        super().__init__(nome)
        self.salariobruto=salariobruto

    def calcular(self):
        self.salario=self.salariobruto-(self.salario_bruto*self.inss/100)

f1=Horista('Jorge', 15,200)
f1.calcular()
#inspect(f1)
f1.analisar()
f2=Mensalista('Jorge', )
f2.calcular()
f2.analisar()