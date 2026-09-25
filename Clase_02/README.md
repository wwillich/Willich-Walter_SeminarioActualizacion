# Clase 02 — Preparación del entorno de desarrollo

## Objetivo

Dejar listo el entorno de trabajo del proyecto integrador:

1. Verificar que Python, VS Code y Git funcionan y que Git está configurado con nombre y email.
2. Crear el proyecto con `app.py` y `README.md`.
3. Crear un entorno virtual `.venv`, activarlo y seleccionarlo como intérprete en VS Code.
4. Instalar una librería (Gradio) y registrar las dependencias en `requirements.txt`.
5. Versionar con Git: `.gitignore` y primer commit.

## Contenido de la carpeta

| Archivo | Descripción | ¿Se versiona? |
|---|---|---|
| `app.py` | App mínima en Gradio: recibe un nombre y devuelve un saludo | Sí |
| `requirements.txt` | Dependencias del entorno (`pip freeze`) | Sí |
| `.gitignore` | Excluye `.venv/`, `__pycache__/` y `.gradio/` | Sí |
| `README.md` | Este archivo | Sí |
| `.venv/` | Entorno virtual local | No |

## Requisitos

- Python 3.10 o superior (probado con Python 3.13)
- Git
- VS Code con la extensión de Python

Para verificar:

```powershell
python --version
git --version
git config user.name
git config user.email
```

Si Git no tiene nombre o email configurados:

```powershell
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

## Cómo reproducirlo

Desde PowerShell, parado en esta carpeta (`Clase_02`):

```powershell
# 1. Crear el entorno virtual
python -m venv .venv

# 2. Activarlo
.\.venv\Scripts\Activate.ps1

# 3. Comparar rutas: con el entorno activo, python debe apuntar a .venv
(Get-Command python).Source
python -c "import sys; print(sys.executable)"

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar la app
python app.py
```

> Si PowerShell bloquea la activación del entorno virtual, ejecutar una vez:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

Para seleccionar el intérprete en VS Code: `Ctrl+Shift+P` → **Python: Select Interpreter** → elegir `Clase_02\.venv\Scripts\python.exe`.

Así se generó `requirements.txt` desde cero:

```powershell
pip install gradio
pip freeze > requirements.txt
```

## Resultado esperado

- Con el entorno activo, `python` apunta a `Clase_02\.venv\Scripts\python.exe`.
- `python app.py` levanta la interfaz en `http://127.0.0.1:7860`.
- Si ingresás un nombre, la app responde `Hola, <nombre>!`. Si el campo queda vacío, responde `Hola!`.
- `git status` no muestra la carpeta `.venv/`, porque está excluida en `.gitignore`.
