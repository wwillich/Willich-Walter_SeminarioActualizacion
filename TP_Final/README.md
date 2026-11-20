# DiabeTrack – TP Final Integrador

**Seminario de Actualización · IFTS N.º 18 · 2026**

## Descripción

DiabeTrack es una aplicación web educativa que utiliza un modelo de Machine Learning para estimar la progresión de la diabetes a partir de tres variables: edad, índice de masa corporal (BMI) y presión arterial media (BP).

El proyecto integra un modelo de regresión lineal desarrollado con Scikit-learn, una API construida con FastAPI y una interfaz web desarrollada con HTML, CSS y JavaScript.

La aplicación tiene fines exclusivamente educativos. Sus resultados no constituyen un diagnóstico médico.

## Tecnologías utilizadas

- **Python:** lenguaje utilizado para el backend y el entrenamiento del modelo.
- **Scikit-learn:** entrenamiento del modelo de regresión lineal.
- **Joblib:** almacenamiento y carga del modelo entrenado.
- **FastAPI:** desarrollo de la API.
- **Pydantic:** validación de los datos recibidos.
- **HTML:** estructura del frontend.
- **CSS:** diseño y estilos de la interfaz.
- **JavaScript:** envío de solicitudes HTTP mediante Fetch API.
- **JSON:** formato de intercambio de información entre frontend y backend.

## Arquitectura del proyecto

```text
TP_Final/
│
├── app/
│   ├── frontend/
│   │   ├── index.html
│   │   ├── style.css
│   │   └── script.js
│   │
│   ├── backend/
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   └── tests/
│   │       └── test_api.py
│   │
│   └── modelo/
│       └── modelo.joblib
│
├── notebook/
│   └── entrenamiento.ipynb
│
├── docs/
│   └── prueba_cors.html
│
├── .gitignore
└── README.md
```

## Modelo de Machine Learning

Se utiliza un modelo de regresión lineal entrenado con el conjunto de datos de diabetes disponible en Scikit-learn.

Las variables de entrada son:

| Variable | Descripción |
|---|---|
| age | Edad en años |
| bmi | Índice de masa corporal |
| bp | Presión arterial media |

El modelo genera una estimación cuantitativa de la progresión de la enfermedad a un año.

El archivo entrenado se almacena en `app/modelo/modelo.joblib` y es cargado por el backend al iniciar la API.

## API

La aplicación dispone de dos endpoints principales:

### GET /health

Comprueba el estado de funcionamiento de la API.

Respuesta:

```json
{
  "estado": "ok"
}
```

### POST /predecir

Recibe los datos de entrada y devuelve la estimación del modelo.

Ejemplo de entrada:

```json
{
  "age": 50,
  "bmi": 27.1,
  "bp": 93
}
```

Ejemplo de respuesta:

```json
{
  "prediccion": 156.4,
  "descripcion": "Progresión estimada de la diabetes a 1 año"
}
```

La API utiliza Pydantic para validar los datos y contempla respuestas HTTP 422 para errores de validación y 500 para errores internos.

## Ejecución local

### 1. Crear y activar el entorno virtual

Desde la carpeta raíz del proyecto:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Instalar las dependencias

```powershell
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

### 3. Iniciar el backend

```powershell
cd app/backend
python -m uvicorn main:app --reload
```

La API estará disponible en:

- API: http://127.0.0.1:8000
- Documentación interactiva: http://127.0.0.1:8000/docs
- Estado: http://127.0.0.1:8000/health

### 4. Iniciar el frontend

En otra terminal, desde la carpeta raíz:

```powershell
cd app/frontend
python -m http.server 5500
```

Abrir en el navegador:

http://127.0.0.1:5500

## CORS

La API utiliza `CORSMiddleware` para permitir la comunicación entre el frontend y el backend cuando se ejecutan desde distintos orígenes.

Los orígenes locales autorizados se configuran mediante la variable de entorno `ALLOWED_ORIGINS`.

## Despliegue

- **Frontend:** https://lukit4as.github.io/portfolio-seminario/
- **Backend:** https://portfolio-seminario-1.onrender.com
- **Documentación de la API:** https://portfolio-seminario-1.onrender.com/docs