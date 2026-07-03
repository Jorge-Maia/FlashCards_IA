from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min:int=1
    canal_max:int=6
    volume_min:int=1
    volume_max:int=5

    def __init__(self, canal=1,volume=1):
        self.canal_atual: int= canal
        self.volume_atual: int = volume
        self.ligado:bool = False

    def liga_desliga(self):
        self.ligado= not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual==ControleRemoto.canal_max:
                self.canal_atual= ControleRemoto.canal_min
            else:
                self.canal_atual+=1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual==ControleRemoto.canal_min:
                self.canal_atual= ControleRemoto.canal_max
            else:
                self.canal_atual-=1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual==ControleRemoto.volume_max:
                self.volume_atual= ControleRemoto.volume_max
            else:
                self.volume_atual+=1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual==ControleRemoto.volume_min:
                self.volume_atual= ControleRemoto.volume_min
            else:
                self.volume_atual-=1

    def mostrartv(self):
        conteudo=''
        if self.ligado==False:
            conteudo=f':prohibited: [red]A TV está desligada[/]'

        else:
            conteudo=f'CANAL= '
            for canal in range(ControleRemoto.canal_min,ControleRemoto.canal_max+1):
                if canal==self.canal_atual:
                    conteudo+=f'[black on yellow] {canal} [/]'
                else:
                    conteudo+=f' {canal}'
            conteudo+=f'\nVOLUME= '
            for volume in range (self.volume_min,self.volume_max+1):
                if volume<=self.volume_atual:
                    conteudo+=f'[black on cyan] [/]'
                else:
                    conteudo+=f'[black on white] [/]'


        tv=Panel(conteudo,title='[ TV ]',width=30)
        print(tv)

c1 = ControleRemoto(3,3)
while True:
    c1.mostrartv()
    r=str(input(f' < CH >   - VOL + '))
    match r:
        case '0':
            break
        case '@':
            c1.liga_desliga()
        case '+':
            c1.volume_mais()
        case '-':
            c1.volume_menos()
        case '>':
            c1.canal_mais()
        case '<':
            c1.canal_menos()
    print('\n'*10)

