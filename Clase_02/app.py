import gradio as gr


def saludar(nombre):
    return f"Hola, {nombre}!" if nombre else "Hola!"


demo = gr.Interface(
    fn=saludar,
    inputs=gr.Textbox(label="Nombre", placeholder="Escribe tu nombre..."),
    outputs=gr.Textbox(label="Saludo"),
    title="App Minimalista",
)

if __name__ == "__main__":
    demo.launch()
