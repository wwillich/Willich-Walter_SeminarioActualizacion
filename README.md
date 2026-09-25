# Seminario de Actualización — Portfolio del proyecto integrador

**Autor:** Walter Willich
**Carrera:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial (IFTS N.º 18), 5.º cuatrimestre

## Resumen

Este repositorio reúne los entregables técnicos del Seminario de Actualización, organizados por clase. Cada carpeta es autocontenida: tiene su propio README con el objetivo, los requisitos y los pasos para reproducir lo que se hizo.

La Clase 01 no tuvo entregable técnico, por eso el índice empieza en la Clase 02.

## Índice

| Clase | Tema | Carpeta |
|---|---|---|
| 02 | Preparación del entorno de desarrollo: Python, Git, entorno virtual y app mínima en Gradio | [Clase_02](Clase_02/) |
| 03 | — | Pendiente |
| 04 | — | Pendiente |
| 05 | — | Pendiente |

## Estado actual

- [x] Clase 02 — Entorno de desarrollo
- [ ] Clase 03
- [ ] Clase 04
- [ ] Clase 05

## Requisitos generales

- Python 3.10 o superior
- Git
- VS Code con la extensión de Python
- Windows con PowerShell (los comandos de los README usan esa sintaxis)

Cada clase usa su propio entorno virtual (`.venv/`, que no se versiona) y su propio `requirements.txt`. Para reproducir una clase:

```powershell
git clone https://github.com/wwillich/Willich-Walter_SeminarioActualizacion.git
cd Willich-Walter_SeminarioActualizacion\Clase_02
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Después, seguí el README de esa carpeta.
