# TP Integrador — Detección de emociones en el chat de un centro de fertilidad

## Objetivo

Construir una aplicación que lee un mensaje antes de que el bot lo conteste, detecta la emoción con un modelo ya entrenado (se infiere, no se entrena) y decide quién responde: el bot o una persona del centro.

## Qué hace y qué no hace la aplicación

- **Hace:** recibe un mensaje de texto, calcula puntajes de emoción con un modelo de Hugging Face y aplica una regla propia: si hay una emoción negativa por encima del umbral, indica **derivar a una persona**; si no, indica que **responde el bot**.
- **No hace:** no se conecta a WhatsApp (simula ese paso), no le contesta a la paciente y no diagnostica nada.
- **Datos:** todos los mensajes de prueba son inventados. La aplicación no está pensada para cargar datos reales de pacientes.

## Aplicación publicada

[willich-walter-seminarioactualizacion.onrender.com](https://willich-walter-seminarioactualizacion.onrender.com/)

> **Nota:** la aplicación usa el plan gratuito de Render, que suspende el servicio después de 15 minutos sin tráfico. Si estaba inactiva, el primer acceso puede demorar alrededor de un minuto mientras el servidor se reinicia.

Por ahora está publicada la versión mínima, que devuelve el mismo mensaje que se escribe. El modelo se suma en una etapa posterior.

### Configuración en Render

| Campo | Valor |
|---|---|
| Repositorio | `wwillich/Willich-Walter_SeminarioActualizacion` |
| Branch | `main` |
| Root Directory | `TP_Integrador` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `python app.py` |
| Instance Type | Free |

## Contenido de la carpeta

| Archivo | Descripción |
|---|---|
| `app.py` | Aplicación de Gradio Blocks: un cuadro de texto, un botón y la función `analizar`, que por ahora devuelve el mismo mensaje |
| `requirements.txt` | Dependencia mínima para el deploy: `gradio` |
| `requirements_notebook.txt` | Dependencias para correr la notebook en local: `transformers`, `torch`, `huggingface_hub`, `pandas`, `psutil` e `ipykernel`. La aplicación publicada no las necesita |
| `README.md` | Este archivo, que se amplía a medida que avanza el trabajo |
| `BITACORA.md` | Errores encontrados durante el trabajo, con su causa y su resolución |
| `.gitignore` | Excluye `.venv/`, `__pycache__/`, `.gradio/` y `.env` |

## Requisitos

- Python 3.10 o superior
- Git
- Windows con PowerShell

## Preparar el entorno

```powershell
git clone https://github.com/wwillich/Willich-Walter_SeminarioActualizacion.git
cd Willich-Walter_SeminarioActualizacion\TP_Integrador
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ejecutar la aplicación en local

```powershell
python app.py
```

La aplicación queda disponible en `http://127.0.0.1:7860`. Si la variable `PORT` está definida (como en Render), usa ese puerto.
