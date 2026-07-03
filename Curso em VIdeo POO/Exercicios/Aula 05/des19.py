from rich import print

class Livro:
    def __init__(self,titulo,páginas):
        self.titulo = titulo
        self.paginas= páginas
        self.paginasatual=1
        print(f'Você pegou o livro [red]{self.titulo}[/], que tem {self.paginas} páginas no total. Você está na pagina 1')


    def avancar(self,valor):
        if self.paginasatual + valor > self.paginas:
            valor = self.paginas - self.paginasatual

        for c in range(self.paginasatual,self.paginasatual+valor):
                print(f'Pág {c} -> ', end='')
        self.paginasatual += valor
        print(f'[blue] Você avançou {valor} páginas e agora está na [/][yellow]página {self.paginasatual}[/]')

        if self.paginasatual == self.paginas:
            print(f':stop_sign:[red] Você chegou ao final do livro {self.titulo}')


l1=Livro('Percy Jackson',130)
l1.avancar(5)
l1.avancar(10)
l1.avancar(20)
l1.avancar(90)
l1.avancar(30)