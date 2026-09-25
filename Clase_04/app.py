import gradio as gr


def saludar(nombre):
    return f"Hola, {nombre}!" if nombre else "Hola!"


def convertir_temperatura(celsius, unidad):
    """Convierte grados Celsius a la unidad elegida."""
    if unidad == "Fahrenheit":
        return round(celsius * 9 / 5 + 32, 2)
    return round(celsius + 273.15, 2)  # Kelvin


with gr.Blocks(title="App Clase 04") as demo:
    gr.Markdown("# App Clase 04\nInterfaz construida con `gr.Blocks`.")

    with gr.Tab("Saludo"):
        nombre = gr.Textbox(label="Nombre", placeholder="Escribí tu nombre...")
        boton_saludo = gr.Button("Saludar", variant="primary")
        saludo = gr.Textbox(label="Saludo", interactive=False)
        boton_saludo.click(fn=saludar, inputs=nombre, outputs=saludo)

    with gr.Tab("Conversor de temperatura"):
        with gr.Row():
            celsius = gr.Slider(minimum=-50, maximum=150, value=25, step=0.5, label="Temperatura (°C)")
            unidad = gr.Radio(["Fahrenheit", "Kelvin"], value="Fahrenheit", label="Convertir a")
        boton_convertir = gr.Button("Convertir", variant="primary")
        resultado = gr.Number(label="Resultado", interactive=False)
        boton_convertir.click(fn=convertir_temperatura, inputs=[celsius, unidad], outputs=resultado)

if __name__ == "__main__":
    demo.launch(share=True)
