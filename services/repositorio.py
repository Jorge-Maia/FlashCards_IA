import sqlite3
from models.deck import Deck
from models.flashcard import Flashcard

class RepositorioFlashcards:
    def __init__(self, caminho_db="flashcards.db"):
        self.caminho_db = caminho_db
        self._criar_tabelas()

    def _conectar(self):
        return sqlite3.connect(self.caminho_db)

    def _criar_tabelas(self):
        conexao = self._conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS decks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS flashcards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                deck_id INTEGER NOT NULL,
                pergunta TEXT NOT NULL,
                resposta TEXT NOT NULL,
                acertos INTEGER DEFAULT 0,
                erros INTEGER DEFAULT 0,
                FOREIGN KEY (deck_id) REFERENCES decks (id)
            )
        """)

        conexao.commit()
        conexao.close()

    def salvar_deck(self, deck):
        conexao = self._conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO decks (titulo) VALUES (?)",
            (deck.titulo,)
        )
        deck_id = cursor.lastrowid

        for card in deck:
            cursor.execute(
                "INSERT INTO flashcards (deck_id, pergunta, resposta, acertos, erros) VALUES (?, ?, ?, ?, ?)",
                (deck_id, card.pergunta, card.resposta, card.acertos, card.erros)
            )

        conexao.commit()
        conexao.close()
        return deck_id

    def listar_decks(self):
        conexao = self._conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, titulo FROM decks")
        resultado = cursor.fetchall()
        conexao.close()
        return resultado

    def carregar_deck(self, deck_id):
        conexao = self._conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT titulo FROM decks WHERE id = ?", (deck_id,))
        titulo = cursor.fetchone()[0]

        cursor.execute(
            "SELECT id, pergunta, resposta, acertos, erros FROM flashcards WHERE deck_id = ? ORDER BY id",
            (deck_id,)
        )
        linhas = cursor.fetchall()
        conexao.close()

        deck = Deck(titulo)
        for flashcard_id, pergunta, resposta, acertos, erros in linhas:
            deck.adicionar_card(pergunta, resposta)
            card = deck[len(deck) - 1]
            card.id = flashcard_id  # guardamos o id da linha no banco
            card.acertos = acertos
            card.erros = erros

        return deck

    def atualizar_estatisticas(self, flashcard_id, acertos, erros):
        conexao = self._conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE flashcards SET acertos = ?, erros = ? WHERE id = ?",
            (acertos, erros, flashcard_id)
        )
        conexao.commit()
        conexao.close()

    def deletar_deck(self, deck_id):
        conexao = self._conectar()
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM flashcards WHERE deck_id = ?", (deck_id,))
        cursor.execute("DELETE FROM decks WHERE id = ?", (deck_id,))

        conexao.commit()
        conexao.close()