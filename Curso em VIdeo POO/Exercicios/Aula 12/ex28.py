from rich import print,inspect

class Termostato:
    def __init__(self):
        self.__temperatura=24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self,temp):

        if temp%0.5!=0:
            raise ValueError (f'Temperatura {temp} inválida!')

        if temp>30:
            self.__temperatura=30

        elif temp<16:
            self.__temperatura=16

        else:
            self.__temperatura=temp

    @property
    def ftemperatura(self):
        return f'{self.__temperatura}°C'

t=Termostato()
try:
    t.temperatura=25.7
except Exception as e:
    print(f'Houve um problema: {e}')

print(f'O termostato está marcando {t.ftemperatura}')

inspect(t,private=True)