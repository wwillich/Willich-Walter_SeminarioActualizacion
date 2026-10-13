import os

import gradio as gr


def analizar(mensaje):
    # Versión mínima: devuelve el mismo texto — el modelo se suma en la fase 4
    return mensaje


with gr.Blocks(title="TP Integrador - Emociones en el chat") as demo:
    gr.Markdown(
        "# TP Integrador — Emociones en el chat de un centro de fertilidad\n"
        "Versión mínima para probar el deploy. Por ahora devuelve el mismo mensaje."
    )
    mensaje = gr.Textbox(label="Mensaje", placeholder="Escribí un mensaje de prueba...")
    boton = gr.Button("Analizar", variant="primary")
    resultado = gr.Textbox(label="Resultado", interactive=False)
    boton.click(fn=analizar, inputs=mensaje, outputs=resultado)

if __name__ == "__main__":
    # En Render: escuchar en todas las interfaces y en el puerto que asigna la plataforma (variable PORT)
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860)),
    )
