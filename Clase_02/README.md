# Clase 02 — Preparación del entorno de desarrollo

## Objetivo

En esta clase dejé armado el entorno con el que voy a trabajar el resto del proyecto:

1. Verifiqué que Python, VS Code y Git funcionan, y que Git está configurado con mi nombre y mail.
2. Creé el proyecto con `app.py` y `README.md`.
3. Armé el entorno virtual `.venv`, lo activé, comparé las rutas del intérprete y lo seleccioné en VS Code.
4. Instalé Gradio en el entorno y generé el `requirements.txt`.
5. Inicialicé el repo, creé el `.gitignore` e hice el primer commit.

## Contenido de la carpeta

| Archivo | Qué tiene | ¿Se versiona? |
|---|---|---|
| `app.py` | App mínima en Gradio: le pasás un nombre y te saluda | Sí |
| `requirements.txt` | Dependencias del entorno, sacadas con `pip freeze` | Sí |
| `.gitignore` | Deja afuera `.venv/`, `__pycache__/` y `.gradio/` | Sí |
| `README.md` | Este archivo | Sí |
| `.venv/` | Entorno virtual local | No |

## Requisitos

- Python 3.10 o superior (yo usé 3.13)
- Git
- VS Code con la extensión de Python

Para chequear que está todo:

```powershell
python --version
git --version
git config user.name
git config user.email
```

Si Git no tiene nombre o mail configurados:

```powershell
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

## Cómo reproducirlo

En PowerShell, parado en la carpeta `Clase_02`:

```powershell
# 1. Crear el entorno virtual
python -m venv .venv

# 2. Activarlo
.\.venv\Scripts\Activate.ps1

# 3. Comparar rutas: con el entorno activo, python tiene que apuntar a .venv
(Get-Command python).Source
python -c "import sys; print(sys.executable)"

# 4. Instalar las dependencias
pip install -r requirements.txt

# 5. Levantar la app
python app.py
```

> Si PowerShell no te deja activar el entorno, corré esto una sola vez:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

Para seleccionar el intérprete en VS Code: `Ctrl+Shift+P` → **Python: Select Interpreter** → `Clase_02\.venv\Scripts\python.exe`.

El `requirements.txt` lo generé así:

```powershell
pip install gradio
pip freeze > requirements.txt
```

## Resultado esperado

- Con el entorno activo, `python` apunta a `Clase_02\.venv\Scripts\python.exe`.
- `python app.py` levanta la interfaz en `http://127.0.0.1:7860`.
- Si ponés un nombre, responde `Hola, <nombre>!`. Si lo dejás vacío, responde `Hola!`.
- `git status` no muestra `.venv/`, porque está en el `.gitignore`.
