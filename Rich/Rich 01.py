from rich import print
from rich.panel import Panel #Add Painel
from rich.table import Table #Add Tabela
from rich import inspect  #Mostra as caracteristicas de uma forma melhor
from rich.traceback import install

install()
print('Ola ,[bold blue on white]mundo[/]! :earth_americas:')

#Para ver os emojis : python -m rich.emoji

caixa=Panel('[white]Esse aqui é um painel de exemplo[\]',title='Exemplo',style='bold blue',width=35)
print(caixa)

tabela=Table(title='Exemplo',style='bold blue',width=35)
tabela.add_column('Nome',justify='center',width=35,style='bold blue')
tabela.add_column('Preço',justify='center',width=35,style='bold red')

tabela.add_row('Lápis','R$5,00')
print(tabela)
inspect(int,all=True)

def divisao(x,y):
    return x/y
print(divisao(50,))