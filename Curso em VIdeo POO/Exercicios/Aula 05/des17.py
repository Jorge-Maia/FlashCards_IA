from rich.panel import Panel
from rich import print

class Produto:
    def __init__(self,nome, valor):
        self.nome = nome
        self.valor = valor
        self.cont=len(self.nome)+30

    def etiqueta(self):
        conteudo= f"{self.nome.center(30, ' ')}"
        conteudo+=f'-'*30
        preçof= f"R${self.valor:.2f}"
        conteudo+=f' {preçof.center(30, '.')}'
        etiqueta=Panel(conteudo, title='Produto',width=35)
        print(etiqueta)




p1=Produto('Iphone 17', 20000)
p1.etiqueta()

p2=Produto('Notebook gamer', 3000)
p2.etiqueta()