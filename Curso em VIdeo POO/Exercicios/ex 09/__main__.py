from ex09 import *
from rich import print,inspect

def main():
    av1=Avaliação('Jorge', "Matemática")
    av1.set_nota(7.2)
    print(f'{av1.nome} tirou {av1._nota} em {av1.disciplina}')
    inspect(av1,private=True)

if __name__ == '__main__':
    main()