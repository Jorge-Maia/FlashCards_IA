from models.flashcard import Flashcard


class Deck:
    def __init__(self, titulo):
        self.titulo = titulo
        self.__cards = []

    def adicionar_card(self, pergunta, resposta):
        novo_card = Flashcard(pergunta, resposta)
        self.__cards.append(novo_card)
        print(f'Card adicionado ao deck {self.titulo}!')

    def listar_cards(self):
        if len(self.__cards) == 0:
            print('Deck vazio!')
            return
        for i, card in enumerate(self.__cards, 1):
            print(f'Card {i}:')
            print(card)

    def __len__(self):
        return len(self.__cards)

    def __getitem__(self, index):
        return self.__cards[index]

    def __str__(self):
        return f'Deck: {self.titulo} | {len(self)} cards'
