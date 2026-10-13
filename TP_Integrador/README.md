# TP Integrador — Detección de emociones en el chat de un centro de fertilidad

## Objetivo

Construir una aplicación que lee un mensaje antes de que el bot lo conteste, detecta la emoción con un modelo ya entrenado (se infiere, no se entrena) y decide quién responde: el bot o una persona del centro.

## Qué hace y qué no hace la aplicación

- **Hace:** recibe un mensaje de texto, calcula puntajes de emoción con un modelo de Hugging Face y aplica una regla propia: si hay una emoción negativa por encima del umbral, indica **derivar a una persona**; si no, indica que **responde el bot**.
- **No hace:** no se conecta a WhatsApp (simula ese paso), no le contesta a la paciente y no diagnostica nada.
- **Datos:** todos los mensajes de prueba son inventados. La aplicación no está pensada para cargar datos reales de pacientes.

## Contenido de la carpeta

| Archivo | Descripción |
|---|---|
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
```
