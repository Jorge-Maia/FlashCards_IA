class Flashcard:
    total_criados = 0

    def __init__(self, pergunta, resposta):
        self.pergunta = pergunta
        self.resposta = resposta
        self.acertos = 0
        self.erros = 0
        self.__revisado = False
        Flashcard.total_criados += 1

    @property
    def revisado(self):
        return self.__revisado

    def marcar_acerto(self):
        self.acertos += 1
        self.__revisado = True

    def marcar_erro(self):
        self.erros += 1
        self.__revisado = True

    def resetar(self):
        self.acertos = 0
        self.erros = 0
        self.__revisado = False

    def __str__(self):
        return f'Pergunta: {self.pergunta} | Resposta: {self.resposta}'

    def __repr__(self):
        return f'Flashcard({self.pergunta}, acertos={self.acertos})'
