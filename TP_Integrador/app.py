import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Analizador de sentimientos",
    page_icon="🎬",
    layout="centered"
)

MODELO = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"


@st.cache_resource
def cargar_modelo():
    return pipeline(
        "sentiment-analysis",
        model=MODELO
    )


st.title("🎬 Analizador de sentimientos")
st.write(
    "Esta aplicación analiza opiniones sobre películas "
    "y estima si el sentimiento expresado es positivo o negativo."
)

st.info(
    "El modelo fue entrenado para textos en inglés. "
    "Las frases en español pueden producir resultados poco fiables."
)

texto = st.text_area(
    "Escribí tu opinión sobre una película:",
    placeholder="Example: This movie was absolutely amazing!"
)

if st.button("Analizar sentimiento", type="primary"):
    if not texto.strip():
        st.warning("Primero escribí una frase.")
    else:
        try:
            with st.spinner("Analizando el texto... La primera carga puede tardar."):
                modelo = cargar_modelo()
                resultado = modelo(texto.strip(), truncation=True)[0]

            etiqueta = resultado["label"]
            confianza = resultado["score"]

            if etiqueta == "POSITIVE":
                st.success("Sentimiento estimado: POSITIVO")
            else:
                st.error("Sentimiento estimado: NEGATIVO")

            st.metric("Confianza del modelo", f"{confianza:.2%}")
            st.caption(
                "La confianza es una estimación del modelo, "
                "no una garantía de que la interpretación sea correcta."
            )

        except Exception as error:
            st.error("No se pudo analizar el texto.")
            st.exception(error)

st.divider()
st.caption(f"Modelo utilizado: {MODELO}")
st.caption("Proyecto integrador — Seminario de Actualización")
