from rich.panel import Panel
from rich import print

class Churrasco:

    def __init__(self,título,quantidade):
        self.titulo=título
        self.quantidade=quantidade

    def analisar(self):
        custo=(self.quantidade*0.4)*82.40
        conteudo= f"Analisando [green]{self.titulo}[/] com [blue]{self.quantidade} convidados[/]!\n"
        conteudo+=f"Cada participante irá comer 0.4Kg e cada Kg custa R$82,40! \n"
        conteudo+=f"Recomendo comprar [blue]{self.quantidade*0.4:.2f}[/] Kg de carne\n"
        conteudo+=f"O custo total será de [green]R${custo:.2f}[/] \n"
        conteudo+=f"Cada pessoa pagará [yellow]R${custo/self.quantidade:.2f}[/] para participar! \n"
        etiqueta=Panel(conteudo, title=self.titulo, width=70)
        print(etiqueta)

p1=Churrasco('Churrasco dos Amigos',15)
p1.analisar()
p2=Churrasco('Churrasco dos Besta',50)
p2.analisar()