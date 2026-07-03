import streamlit as st
from services.gerador_ia import GeradorIA
from services.repositorio import RepositorioFlashcards
from models.deck import Deck

st.title("🧠 Gerador de Flashcards com IA")
st.write("Digite um tema e a IA vai criar flashcards de estudo pra você.")

repositorio = RepositorioFlashcards()

if "deck" not in st.session_state:
    st.session_state.deck = None

# --- Barra lateral: decks já salvos ---
st.sidebar.header("📚 Decks salvos")

decks_salvos = repositorio.listar_decks()

if not decks_salvos:
    st.sidebar.write("Nenhum deck salvo ainda.")
else:
    for deck_id, titulo in decks_salvos:
        col_nome, col_deletar = st.sidebar.columns([4, 1])

        with col_nome:
            if st.button(titulo, key=f"carregar_{deck_id}"):
                st.session_state.deck = repositorio.carregar_deck(deck_id)

        with col_deletar:
            if st.button("🗑️", key=f"deletar_{deck_id}"):
                st.session_state.confirmando_delete = deck_id
                st.rerun()

    # Confirmação de exclusão
    if st.session_state.get("confirmando_delete") is not None:
        deck_id_apagar = st.session_state.confirmando_delete
        st.sidebar.warning("Tem certeza que quer apagar este deck?")
        col_sim, col_nao = st.sidebar.columns(2)
        with col_sim:
            if st.button("Sim, apagar", key="confirma_sim"):
                repositorio.deletar_deck(deck_id_apagar)
                st.session_state.confirmando_delete = None
                if st.session_state.deck is not None and hasattr(st.session_state.deck[0], "id"):
                    st.session_state.deck = None
                st.rerun()
        with col_nao:
            if st.button("Cancelar", key="confirma_nao"):
                st.session_state.confirmando_delete = None
                st.rerun()

# --- Área principal: gerar um novo deck ---
tema = st.text_input("Qual o tema dos flashcards?")
quantidade = st.number_input("Quantos flashcards?", min_value=1, max_value=10, value=5)

if st.button("Gerar flashcards"):
    if tema.strip() == "":
        st.warning("Digite um tema antes de gerar!")
    else:
        with st.spinner("A IA está criando seus flashcards..."):
            gerador = GeradorIA()
            dados = gerador.gerar_flashcards(tema, quantidade)

            novo_deck = Deck(tema)
            for item in dados:
                novo_deck.adicionar_card(item["pergunta"], item["resposta"])

            st.session_state.deck = novo_deck

# --- Exibindo o deck atual, com opção de salvar ---
if st.session_state.deck is not None:
    st.subheader(f"Deck: {st.session_state.deck.titulo}")

    if st.button("💾 Salvar deck no banco"):
        repositorio.salvar_deck(st.session_state.deck)
        st.success("Deck salvo com sucesso!")
        st.rerun()

    for i, card in enumerate(st.session_state.deck, 1):
        with st.expander(f"Card {i}: {card.pergunta}"):
            st.write(card.resposta)

# --- Modo de estudo ---
if st.session_state.deck is not None and hasattr(st.session_state.deck[0], "id"):
    st.divider()
    st.subheader("📖 Modo de estudo")

    if "indice_estudo" not in st.session_state:
        st.session_state.indice_estudo = 0
    if "mostrar_resposta" not in st.session_state:
        st.session_state.mostrar_resposta = False

    deck_estudo = st.session_state.deck
    total = len(deck_estudo)
    indice = st.session_state.indice_estudo

    if indice >= total:
        st.success("Você revisou todos os cards deste deck! 🎉")
        if st.button("Estudar de novo"):
            st.session_state.indice_estudo = 0
            st.session_state.mostrar_resposta = False
            st.rerun()
    else:
        card_atual = deck_estudo[indice]

        st.progress((indice) / total, text=f"Card {indice + 1} de {total}")
        st.write(f"**Pergunta:** {card_atual.pergunta}")

        if not st.session_state.mostrar_resposta:
            if not st.session_state.mostrar_resposta:
                if st.button("Mostrar resposta", key=f"mostrar_{indice}"):
                    st.session_state.mostrar_resposta = True
                    st.rerun()
        else:
            st.info(f"**Resposta:** {card_atual.resposta}")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Acertei", key=f"acertei_{indice}"):
                    card_atual.marcar_acerto()
                    repositorio.atualizar_estatisticas(
                        card_atual.id, card_atual.acertos, card_atual.erros
                    )
                    st.session_state.indice_estudo += 1
                    st.session_state.mostrar_resposta = False
                    st.rerun()
            with col2:
                if st.button("❌ Errei", key=f"errei_{indice}"):
                    card_atual.marcar_erro()
                    repositorio.atualizar_estatisticas(
                        card_atual.id, card_atual.acertos, card_atual.erros
                    )
                    st.session_state.indice_estudo += 1
                    st.session_state.mostrar_resposta = False
                    st.rerun()