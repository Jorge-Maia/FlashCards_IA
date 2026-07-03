from rich import print

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.destampada=False

    def escrever(self, texto):
        if not self.destampada:
            print("[red]Erro: a caneta está tampada![/]")
            return
        if self.cor == 'vermelho':
            escrito=f'[red]{texto}[/]'
            print(escrito)
        if self.cor == 'verde':
            escrito=f'[green]{texto}[/]'
            print(escrito)
        if self.cor == 'azul':
            escrito=f'[blue]{texto}[/]'
            print(escrito)

    def quebrar_linha(self,num):
        for c in range(num):
            print()




c1= Caneta('vermelho')
c2= Caneta('verde')
c3= Caneta('azul')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Ola tudo bem')
c1.quebrar_linha(1)
c2.escrever('Ola tudo bem')
c3.escrever('Ola tudo bem')