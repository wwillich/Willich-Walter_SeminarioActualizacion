# Clase 05 — Deploy en Render: Gradio y Streamlit

## Objetivo

En esta clase publicamos la aplicación en un servidor real y comprobamos que el procedimiento de deploy no depende de la herramienta utilizada para la interfaz:

1. **Deploy en Render** de la aplicación de Gradio Blocks desarrollada en la Clase 04.
2. **Versión equivalente en Streamlit**, mínima, publicada con el mismo procedimiento.
3. **Documentación** de ambos deploys y de las diferencias encontradas.

## Aplicaciones publicadas

| Versión | Enlace | Qué hace |
|---|---|---|
| Gradio (Blocks) | [willich-walter-clase-05-gradio.onrender.com](https://willich-walter-clase-05-gradio.onrender.com/) | Dos pestañas: **Saludo** (recibe un nombre y devuelve un saludo al presionar un botón) y **Conversor de temperatura** (convierte °C a Fahrenheit o Kelvin con un slider y un selector de unidad) |
| Streamlit | [willich-walter-clase-05-streamlit.onrender.com](https://willich-walter-clase-05-streamlit.onrender.com/) | Las mismas dos funciones en una versión mínima: saludo con botón y conversor que actualiza el resultado automáticamente al mover el slider |

> **Nota:** ambas aplicaciones usan el plan gratuito de Render, que suspende el servicio después de 15 minutos sin tráfico. Si la aplicación estaba inactiva, el primer acceso puede demorar alrededor de un minuto mientras el servidor se reinicia.

## Diferencias entre Gradio y Streamlit

1. **Configuración del puerto:** en Gradio, el host y el puerto se definen en el código, dentro de `demo.launch(server_name="0.0.0.0", server_port=...)`, leyendo la variable `PORT` que asigna Render. En Streamlit, el código no cambia: esos mismos valores se pasan como parámetros en el comando de inicio.
2. **Modelo de ejecución:** Gradio conecta cada función a sus componentes mediante eventos (`.click()`), mientras que Streamlit vuelve a ejecutar el script completo ante cada interacción. Por eso, en la versión de Streamlit el conversor se actualiza sin necesidad de un botón.
3. **Procedimiento de deploy:** fue idéntico en ambos casos (repositorio, carpeta raíz, comando de build y comando de inicio). La única diferencia fue el comando de inicio, y fue justamente el punto donde surgió un error: el primer deploy de Streamlit se configuró con `python app.py`. Con ese comando, Streamlit ejecuta el script una sola vez sin levantar el servidor web (advertencias `missing ScriptRunContext`) y Render marca el deploy como fallido (`Application exited early`). Se resolvió reemplazándolo por `streamlit run`.

## Contenido de la carpeta

| Archivo | Descripción |
|---|---|
| `gradio_app/app.py` | Aplicación de Gradio Blocks, adaptada para Render (`server_name` y `server_port`) |
| `gradio_app/requirements.txt` | Dependencia mínima para el deploy: `gradio` |
| `streamlit_app/app.py` | Versión mínima de la aplicación en Streamlit |
| `streamlit_app/requirements.txt` | Dependencia mínima para el deploy: `streamlit` |
| `.gitignore` | Excluye `.venv/`, `__pycache__/` y `.gradio/` |
| `README.md` | Este archivo |

Cada aplicación tiene su propio `requirements.txt` con solo lo que necesita. A diferencia de las clases anteriores, no usamos `pip freeze`: la lista completa del entorno local incluye paquetes que dependen de la versión de Python y del sistema operativo, y podría fallar en el servidor de Render, que corre Linux.

## Requisitos

- Python 3.10 o superior (probado localmente con Python 3.13; Render utilizó Python 3.14)
- Cuenta en [Render](https://render.com) vinculada a GitHub (solo para el deploy)

## Cómo reproducirlo

### Ejecución local

Desde PowerShell, en la carpeta `Clase_05`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r gradio_app\requirements.txt -r streamlit_app\requirements.txt

# Gradio -> http://127.0.0.1:7860
python gradio_app\app.py

# Streamlit -> http://localhost:8501
streamlit run streamlit_app\app.py
```

### Deploy en Render

Se crea un **Web Service** por cada aplicación, desde el panel de Render: *New → Web Service → Build and deploy from a Git repository*, y se selecciona este repositorio. La configuración es la misma para ambos servicios, salvo la carpeta raíz y el comando de inicio:

| Campo | Gradio | Streamlit |
|---|---|---|
| Branch | `main` | `main` |
| Root Directory | `Clase_05/gradio_app` | `Clase_05/streamlit_app` |
| Runtime | Python 3 | Python 3 |
| Build Command | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Start Command | `python app.py` | `streamlit run app.py --server.port $PORT --server.address 0.0.0.0` |
| Instance Type | Free | Free |

Render asigna el puerto a través de la variable de entorno `PORT`, y la aplicación tiene que escuchar en `0.0.0.0` para aceptar conexiones externas. Si se deja el valor por defecto (`127.0.0.1`), el servidor solo acepta conexiones internas y Render no detecta ningún puerto abierto, por lo que el deploy falla.

## Resultado esperado

- Cada servicio queda publicado en una dirección del tipo `https://<nombre-del-servicio>.onrender.com`, que funciona sin necesidad de mantener encendido el equipo local.
- **Gradio:** con 25 °C y *Fahrenheit*, el resultado es **77**. Al ingresar un nombre y presionar *Saludar*, responde `Hola, <nombre>!`.
- **Streamlit:** con 100 °C y *Kelvin*, el resultado es **373.15 K**, y se actualiza al mover el slider.
- Ante cada `git push` a `main`, Render vuelve a desplegar automáticamente el servicio.
