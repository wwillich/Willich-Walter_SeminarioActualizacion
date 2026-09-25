# Seminario de Actualización — Portfolio del proyecto integrador

**Walter Willich**
Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial, IFTS N.º 18, 5.º cuatrimestre.

## Resumen

En este repo junto lo que voy haciendo en el Seminario de Actualización, clase por clase. Cada carpeta tiene su propio README donde cuento qué hice, qué hace falta para correrlo y qué debería salir.

La Clase 01 no tuvo entregable técnico, por eso arranco en la 02.

## Índice

| Clase | Tema | Carpeta |
|---|---|---|
| 02 | Preparación del entorno: Python, Git, entorno virtual y una app mínima en Gradio | [Clase_02](Clase_02/) |
| 03 | GitHub, Codespaces y control de versiones: 3 situaciones problema con Git | [Clase_03](Clase_03/) |
| 04 | — | Pendiente |
| 05 | — | Pendiente |

## Estado actual

- [x] Clase 02 — Entorno de desarrollo
- [x] Clase 03 — GitHub y control de versiones
- [ ] Clase 04
- [ ] Clase 05

## Requisitos generales

- Python 3.10 o superior
- Git
- VS Code con la extensión de Python
- Windows con PowerShell (los comandos de los README están escritos para PowerShell)

Cada clase tiene su propio entorno virtual (`.venv/`, que no se sube) y, si lo necesita, su propio `requirements.txt`. Para reproducir una clase:

```powershell
git clone https://github.com/wwillich/Willich-Walter_SeminarioActualizacion.git
cd Willich-Walter_SeminarioActualizacion\Clase_02
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Y después seguí el README de esa carpeta.
