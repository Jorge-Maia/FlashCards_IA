from rich import print
from rich import inspect

class ContaBancaria:
    """
    Cria uma conta bancária que permite fazer saques e depósitos
    """
    def __init__(self,id,nome,saldo=0):
        self.id=id
        self.nome=nome
        self.saldo=saldo
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}')
    def __str__(self):
        return f'A conta {self.id} de {self.nome} tem R${self.saldo:,.2f} de saldo!'

    def depositar(self,valor):
        self.saldo+=valor
        print(f'Depósito autorizado de R${valor:,.2f} na conta de {self.nome}')
    def sacar(self,valor):
        if valor>self.saldo:
            print(f'Saldo insuficiente para saque. Tente novamente!')
        else:
            self.saldo-=valor
            print(f'Saque autorizado de R${valor:,.2f} na conta de {self.nome}')


c1=ContaBancaria(112,"Jorge",3000)
c1.depositar(500)
c1.sacar(1000)
print(c1)
inspect(c1)
