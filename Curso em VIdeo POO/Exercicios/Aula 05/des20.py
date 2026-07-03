from rich.panel import Panel
from rich import print
from rich.console import Console

class Gamer:
    def __init__(self,nome, nick):
        self.nome = nome
        self.nick = nick
        self.favorito = []

    def add_favorito(self,favorito):
        self.favorito.append(favorito)

    def ficha(self):
        conteudo= f'Nome real: [black on blue]{self.nome}[/]\n'
        conteudo += f'Jogos favoritos: \n'
        for favorito in self.favorito:
            conteudo += f':video_game: [blue]{favorito}[/]\n'
        ficha=Panel(conteudo, title=f'Jogador {self.nick}')
        print(ficha)



j1=Gamer('Jorge Maia', 'Antixereca')
j1.add_favorito('God of War')
j1.add_favorito('Fortnite')
j1.add_favorito('Minecraft')
j1.ficha()

j2=Gamer('Jorge Moia', 'Anticu')
j2.add_favorito('Fortnite')
j2.add_favorito('Minecraft')
j2.ficha()