from translate import Translator
import streamlit as st

def traduzir(textos, idioma):
    tradutor = Translator(to_lang=idioma, from_lang='pt-br')

    texto = textos

    traducao = tradutor.translate(texto)

    return "Seu texto traduzido: ", traducao

st.set_page_config(page_title="Tradutor Simples", layout="centered")

st.title("🌍 Tradutor Simples")

texto = st.text_area("Digite o texto que deseja traduzir:")

idioma_destino = st.selectbox(
    "Selecione o idioma em que deseja traduzir:",
    ["en", "es", "fr", "de", "it", "pt"]
)

if st.button("Traduzir"):
    if texto.strip():
        trad = traduzir(texto, idioma_destino)
        st.subheader("🔎 Tradução:")
        st.success(trad)
    else:

        st.warning("Digite um texto para traduzir.")


