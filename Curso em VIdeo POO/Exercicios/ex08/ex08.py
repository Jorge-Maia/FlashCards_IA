from rich import print
from rich import inspect

class ContaBancaria:
    """
    Cria uma conta bancária que permite fazer saques e depósitos
    """
    def __init__(self,id,nome,saldo=0):
        self.id=id
        self._nome=nome
        self.__saldo=saldo
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}')
    def __str__(self):
        #return f'A conta {self.id} de {self.nome} tem R${self.saldo:,.2f} de saldo!'
        return f'Estado atual: {self.__dict__}'

    def depositar(self,valor):
        valor=abs(valor)
        self.__saldo+=valor
        print(f'Depósito autorizado de R${valor:,.2f} na conta de {self._nome}')

    def sacar(self,valor):
        valor=abs(valor)
        if valor>self.__saldo:
            print(f'Saldo insuficiente para saque. Tente novamente!')
        else:
            self.__saldo-=valor
            print(f'Saque autorizado de R${valor:,.2f} na conta de {self._nome}')


