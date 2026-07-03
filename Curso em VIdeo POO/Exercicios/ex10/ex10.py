class Avaliação:
    def __init__(self, nome,disciplina,nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota       #Protegido

    # Criando Atributo Validável
    @property
    def nota(self):  #getter
        return self._nota

    @nota.setter
    def nota(self,valor):
        if 0<=valor<=10:
            self._nota = valor
        else:
            print('Valor invalido')
