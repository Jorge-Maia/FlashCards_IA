''''from models.deck import Deck

# Criando um deck
deck = Deck("Programação Orientada a Objetos")

# Adicionando flashcards
deck.adicionar_card(
    "O que é encapsulamento?",
    "É o conceito de proteger os dados internos de um objeto."
)
deck.adicionar_card(
    "O que é herança?",
    "É quando uma classe filha herda atributos e métodos da classe pai."
)
deck.adicionar_card(
    "O que é polimorfismo?",
    "É quando objetos diferentes respondem ao mesmo método de formas distintas."
)

# Testando os métodos especiais
print(deck)           # chama __str__
print(f"\nTotal de cards: {len(deck)}")  # chama __len__

# Listando os cards
print("\n--- Todos os cards ---")
deck.listar_cards()

# Testando acerto e erro
print("\n--- Simulando uma revisão ---")
deck[0].marcar_acerto()
deck[1].marcar_erro()
print(f"Card 1 - Acertos: {deck[0].acertos}")
print(f"Card 2 - Erros: {deck[1].erros}")

# Atributo de classe
from models.flashcard import Flashcard
print(f"\nTotal de flashcards criados: {Flashcard.total_criados}")'''

'''from services.repositorio import RepositorioFlashcards
from services.gerador_ia import GeradorIA
from models.deck import Deck

repositorio = RepositorioFlashcards()

gerador = GeradorIA()
dados = gerador.gerar_flashcards("Sistema Solar", quantidade=3)

deck = Deck("Sistema Solar")
for item in dados:
    deck.adicionar_card(item["pergunta"], item["resposta"])

deck_id = repositorio.salvar_deck(deck)
print(f"Deck salvo com id {deck_id}!")

print("\n--- Decks salvos no banco ---")
for id_salvo, titulo in repositorio.listar_decks():
    print(f"{id_salvo}: {titulo}")

print("\n--- Recuperando o deck do banco ---")
deck_recuperado = repositorio.carregar_deck(deck_id)
deck_recuperado.listar_cards()'''

from services.repositorio import RepositorioFlashcards

repositorio = RepositorioFlashcards()

for deck_id, titulo in repositorio.listar_decks():
    print(f"\n=== Deck {deck_id}: {titulo} ===")
    deck = repositorio.carregar_deck(deck_id)
    for card in deck:
        print(f"  Pergunta: {card.pergunta}")
        print(f"  Resposta: {card.resposta}")