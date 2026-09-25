# Clase 02 — Preparación del entorno de desarrollo

## Objetivo

En esta clase configuramos el entorno de trabajo que se utiliza en el resto del proyecto:

1. Verificamos que Python, VS Code y Git estén instalados y que Git tenga configurados el nombre y el correo del autor.
2. Creamos el proyecto con `app.py` y `README.md`.
3. Generamos el entorno virtual `.venv`, lo activamos, comparamos las rutas del intérprete y lo seleccionamos en VS Code.
4. Instalamos Gradio dentro del entorno y registramos las dependencias en `requirements.txt`.
5. Inicializamos el repositorio, creamos el `.gitignore` y registramos el primer commit.

## Contenido de la carpeta

| Archivo | Descripción | ¿Se versiona? |
|---|---|---|
| `app.py` | Aplicación mínima en Gradio: recibe un nombre y devuelve un saludo | Sí |
| `requirements.txt` | Dependencias del entorno, generadas con `pip freeze` | Sí |
| `.gitignore` | Excluye `.venv/`, `__pycache__/` y `.gradio/` | Sí |
| `README.md` | Este archivo | Sí |
| `.venv/` | Entorno virtual local | No |

## Requisitos

- Python 3.10 o superior (probado con Python 3.13)
- Git
- VS Code con la extensión de Python

Para verificar la instalación:

```powershell
python --version
git --version
git config user.name
git config user.email
```

Si Git no tiene configurados el nombre o el correo:

```powershell
git config --global user.name "Nombre Apellido"
git config --global user.email "correo@ejemplo.com"
```

## Cómo reproducirlo

Desde PowerShell, en la carpeta `Clase_02`:

```powershell
# 1. Crear el entorno virtual
python -m venv .venv

# 2. Activarlo
.\.venv\Scripts\Activate.ps1

# 3. Comparar rutas: con el entorno activo, el intérprete debe apuntar a .venv
(Get-Command python).Source
python -c "import sys; print(sys.executable)"

# 4. Instalar las dependencias
pip install -r requirements.txt

# 5. Ejecutar la aplicación
python app.py
```

> **Nota:** si PowerShell bloquea la activación del entorno virtual, ejecutar una única vez:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

Para seleccionar el intérprete en VS Code: `Ctrl+Shift+P` → **Python: Select Interpreter** → `Clase_02\.venv\Scripts\python.exe`.

El archivo `requirements.txt` se generó de la siguiente manera:

```powershell
pip install gradio
pip freeze > requirements.txt
```

## Resultado esperado

- Con el entorno activo, `python` apunta a `Clase_02\.venv\Scripts\python.exe`.
- `python app.py` inicia la interfaz en `http://127.0.0.1:7860`.
- Al ingresar un nombre, la aplicación responde `Hola, <nombre>!`. Si el campo queda vacío, responde `Hola!`.
- `git status` no muestra la carpeta `.venv/`, ya que está excluida en el `.gitignore`.
