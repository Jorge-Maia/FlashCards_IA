import os
import requests
from dotenv import load_dotenv
from models.deck import Deck
from models.flashcard import Flashcard

load_dotenv()

TURSO_URL = os.environ.get("TURSO_DATABASE_URL", "").replace("libsql://", "https://")
TURSO_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")


def _formatar_valor(valor):
    if valor is None:
        return {"type": "null"}
    if isinstance(valor, bool):
        return {"type": "integer", "value": "1" if valor else "0"}
    if isinstance(valor, int):
        return {"type": "integer", "value": str(valor)}
    return {"type": "text", "value": str(valor)}


def executar_sql(sql, args=None):
    args_formatados = [_formatar_valor(a) for a in (args or [])]

    resposta = requests.post(
        f"{TURSO_URL}/v2/pipeline",
        headers={
            "Authorization": f"Bearer {TURSO_TOKEN}",
            "Content-Type": "application/json"
        },
        json={
            "requests": [
                {"type": "execute", "stmt": {"sql": sql, "args": args_formatados}},
                {"type": "close"}
            ]
        }
    )
    resposta.raise_for_status()
    dados = resposta.json()
    resultado = dados["results"][0]["response"]["result"]

    colunas = [c["name"] for c in resultado["cols"]]
    linhas = []
    for linha in resultado["rows"]:
        valores = [celula.get("value") for celula in linha]
        linhas.append(dict(zip(colunas, valores)))

    return {
        "linhas": linhas,
        "last_insert_rowid": resultado.get("last_insert_rowid")
    }


class RepositorioFlashcards:
    def __init__(self):
        self._criar_tabelas()

    def _criar_tabelas(self):
        executar_sql("""
            CREATE TABLE IF NOT EXISTS decks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL
            )
        """)
        executar_sql("""
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

    def salvar_deck(self, deck):
        resultado = executar_sql(
            "INSERT INTO decks (titulo) VALUES (?)",
            [deck.titulo]
        )
        deck_id = int(resultado["last_insert_rowid"])

        for card in deck:
            executar_sql(
                "INSERT INTO flashcards (deck_id, pergunta, resposta, acertos, erros) VALUES (?, ?, ?, ?, ?)",
                [deck_id, card.pergunta, card.resposta, card.acertos, card.erros]
            )

        return deck_id

    def listar_decks(self):
        resultado = executar_sql("SELECT id, titulo FROM decks")
        return [(int(linha["id"]), linha["titulo"]) for linha in resultado["linhas"]]

    def carregar_deck(self, deck_id):
        resultado_deck = executar_sql(
            "SELECT titulo FROM decks WHERE id = ?", [deck_id]
        )
        titulo = resultado_deck["linhas"][0]["titulo"]

        resultado_cards = executar_sql(
            "SELECT id, pergunta, resposta, acertos, erros FROM flashcards WHERE deck_id = ? ORDER BY id",
            [deck_id]
        )

        deck = Deck(titulo)
        for linha in resultado_cards["linhas"]:
            deck.adicionar_card(linha["pergunta"], linha["resposta"])
            card = deck[len(deck) - 1]
            card.id = int(linha["id"])
            card.acertos = int(linha["acertos"])
            card.erros = int(linha["erros"])

        return deck

    def atualizar_estatisticas(self, flashcard_id, acertos, erros):
        executar_sql(
            "UPDATE flashcards SET acertos = ?, erros = ? WHERE id = ?",
            [acertos, erros, flashcard_id]
        )

    def deletar_deck(self, deck_id):
        executar_sql("DELETE FROM flashcards WHERE deck_id = ?", [deck_id])
        executar_sql("DELETE FROM decks WHERE id = ?", [deck_id])