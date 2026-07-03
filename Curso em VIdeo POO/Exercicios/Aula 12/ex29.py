from rich import print,inspect

class Diario():
    def __init__(self, senha):
        self.__senha = senha
        self.__segredos= []


    def escrever(self,frase):
        self.__segredos.append(frase)

    def ler(self, senha):
        if senha!= self.__senha:
            raise PermissionError('Senha incorreta! Você não pode ler esse diário!')

        else:
            print(f'Diário LIBERADO')
            for i in self.__segredos:
                print(f'- {i}')

    @property
    def senha(self):
        raise PermissionError('Ninguem pode ver a senha!')




d1=Diario('Giii')
d1.escrever('Jorge é muito bonito')
d1.escrever('UIUIUI')
d1.escrever('Você é muito eficiente e rápido!')
try:
    d1.ler('Giii')
except Exception as e:
    print(f'[red]Erro: {e}')

#inspect(d1,private=True,methods=True)
