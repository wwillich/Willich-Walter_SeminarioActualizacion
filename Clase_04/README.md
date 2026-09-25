# Clase 04 — Interfaz con Gradio Blocks

## Objetivo

En esta clase reemplazamos `gr.Interface` por `gr.Blocks` para tener control sobre la disposición de la interfaz, y ampliamos la aplicación de la Clase 02:

1. **Cambio a Blocks:** la interfaz se construye con `gr.Blocks`, organizada en dos pestañas (`gr.Tab`).
2. **Componentes nuevos:** incorporamos `gr.Slider`, `gr.Radio` y `gr.Number`, que no se habían utilizado en clase (además de `Textbox` y `Button`).
3. **Función propia:** agregamos `convertir_temperatura(celsius, unidad)`, conectada a sus propios inputs (slider y selector de unidad) y a su propio output (campo numérico).
4. **Ejecución y enlace público:** la aplicación se ejecuta localmente con `share=True`, que genera un enlace público temporal para compartirla.

## Contenido de la carpeta

| Archivo | Descripción | ¿Se versiona? |
|---|---|---|
| `app.py` | Aplicación en Gradio Blocks con dos pestañas: saludo y conversor de temperatura | Sí |
| `requirements.txt` | Dependencias del entorno, generadas con `pip freeze` | Sí |
| `.gitignore` | Excluye `.venv/`, `__pycache__/` y `.gradio/` | Sí |
| `README.md` | Este archivo | Sí |
| `.venv/` | Entorno virtual local | No |

### Estructura de la aplicación

| Pestaña | Inputs | Función | Output |
|---|---|---|---|
| Saludo | `Textbox` (nombre) | `saludar(nombre)` | `Textbox` |
| Conversor de temperatura | `Slider` (°C, de -50 a 150) + `Radio` (Fahrenheit / Kelvin) | `convertir_temperatura(celsius, unidad)` | `Number` |

Cada función se ejecuta al presionar su propio `Button`, mediante el evento `.click()`.

## Requisitos

- Python 3.10 o superior (probado con Python 3.13)
- Conexión a internet, necesaria para generar el enlace público de `share=True`

## Cómo reproducirlo

Desde PowerShell, en la carpeta `Clase_04`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Al iniciar, la consola muestra dos direcciones:

- **Local URL** (`http://127.0.0.1:7860`): accesible solo desde el equipo donde se ejecuta.
- **Public URL** (`https://xxxxxxxx.gradio.live`): el enlace temporal generado por `share=True`, accesible desde cualquier dispositivo.

> **Nota:** el enlace público funciona solo mientras la aplicación siga en ejecución y caduca después de un tiempo. Cualquier persona que lo tenga puede usar la aplicación, por lo que conviene compartirlo solo en el aula virtual y no publicarlo en el repositorio.

## Resultado esperado

- La interfaz muestra dos pestañas: **Saludo** y **Conversor de temperatura**.
- **Saludo:** al ingresar un nombre y presionar *Saludar*, responde `Hola, <nombre>!`.
- **Conversor:** con el slider en 25 °C y *Fahrenheit* seleccionado, el resultado es **77**. Con 100 °C y *Kelvin*, el resultado es **373.15**.
- El enlace `gradio.live` abre la misma aplicación desde otro dispositivo (por ejemplo, un celular).
