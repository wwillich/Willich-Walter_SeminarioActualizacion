# Seminario de Actualización — Portfolio del proyecto integrador

**Alumno:** Walter Willich

**Carrera:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial — IFTS N.º 18, 5.º cuatrimestre

## Resumen

Este repositorio reúne los entregables técnicos del Seminario de Actualización, organizados por clase. Cada carpeta es autocontenida e incluye su propio README con el objetivo de la clase, los requisitos y los pasos necesarios para reproducir lo realizado.

La Clase 01 no tuvo entregable técnico, por lo que el índice comienza en la Clase 02.

## Índice

| Clase | Tema | Carpeta |
|---|---|---|
| 02 | Preparación del entorno de desarrollo: Python, Git, entorno virtual y aplicación mínima en Gradio | [Clase_02](Clase_02/) |
| 03 | GitHub, Codespaces y control de versiones: tres situaciones problema con Git | [Clase_03](Clase_03/) |
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
- Windows con PowerShell (los comandos de cada README están escritos para PowerShell)

Cada clase utiliza su propio entorno virtual (`.venv/`, excluido del control de versiones) y, cuando corresponde, su propio `requirements.txt`. Para reproducir una clase:

```powershell
git clone https://github.com/wwillich/Willich-Walter_SeminarioActualizacion.git
cd Willich-Walter_SeminarioActualizacion\Clase_02
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

A partir de ahí, seguir las instrucciones del README de la carpeta correspondiente.
