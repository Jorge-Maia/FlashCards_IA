from ex10 import *
from rich import print,inspect

def main():
    av1=Avaliação('Jorge', "Matemática")
    av1.nota=-7.2
    print(f'{av1.nome} tirou {av1.nota} em {av1.disciplina}')
    inspect(av1,private=True)

if __name__ == '__main__':
    main()