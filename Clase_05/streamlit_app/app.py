import streamlit as st


def saludar(nombre):
    return f"Hola, {nombre}!" if nombre else "Hola!"


def convertir_temperatura(celsius, unidad):
    """Convierte grados Celsius a la unidad elegida."""
    if unidad == "Fahrenheit":
        return round(celsius * 9 / 5 + 32, 2)
    return round(celsius + 273.15, 2)  # Kelvin


st.set_page_config(page_title="App Clase 05 - Streamlit")
st.title("App Clase 05 — Streamlit")
st.write("Versión mínima de la aplicación de Gradio, publicada en Render.")

tab_saludo, tab_conversor = st.tabs(["Saludo", "Conversor de temperatura"])

with tab_saludo:
    nombre = st.text_input("Nombre", placeholder="Escribí tu nombre...")
    if st.button("Saludar"):
        st.success(saludar(nombre))

with tab_conversor:
    celsius = st.slider("Temperatura (°C)", min_value=-50.0, max_value=150.0, value=25.0, step=0.5)
    unidad = st.radio("Convertir a", ["Fahrenheit", "Kelvin"], horizontal=True)
    # Streamlit vuelve a ejecutar el script ante cada cambio: el resultado se actualiza sin botón
    st.metric("Resultado", f"{convertir_temperatura(celsius, unidad)} {'°F' if unidad == 'Fahrenheit' else 'K'}")
