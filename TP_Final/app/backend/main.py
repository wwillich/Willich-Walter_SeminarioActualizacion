"""API FastAPI que sirve el modelo de regresión lineal (diabetes: age, bmi, bp)."""
import logging
import os
from contextlib import asynccontextmanager
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict, Field

logger = logging.getLogger("api")

MODEL_PATH = Path(
    os.getenv("MODEL_PATH", Path(__file__).resolve().parent.parent / "modelo" / "modelo.joblib")
)
ALLOWED_ORIGINS = [
    o.strip()
    for o in os.getenv("ALLOWED_ORIGINS", "http://localhost:5500,http://127.0.0.1:5500").split(",")
    if o.strip()
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    # El modelo se carga una sola vez al arrancar, no en cada request.
    app.state.modelo = joblib.load(MODEL_PATH)
    logger.info("Modelo cargado desde %s", MODEL_PATH)
    yield


app = FastAPI(
    title="API de predicción de progresión de diabetes",
    description="Regresión lineal (scikit-learn) entrenada con el dataset de diabetes. "
    "Entrada: edad, IMC y presión arterial media.",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


class EntradaPrediccion(BaseModel):
    # strict: "50" (string) no se convierte a número -> 422. forbid: campos extra -> 422.
    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        json_schema_extra={"examples": [{"age": 50, "bmi": 27.1, "bp": 93}]},
    )

    age: float = Field(gt=0, le=120, description="Edad en años")
    bmi: float = Field(gt=10, le=70, description="Índice de masa corporal (kg/m²)")
    bp: float = Field(gt=40, le=250, description="Presión arterial media (mmHg)")


class SalidaPrediccion(BaseModel):
    prediccion: float = Field(description="Progresión estimada de la enfermedad a 1 año")
    descripcion: str


@app.get("/health")
def health():
    return {"estado": "ok"}


@app.post("/predecir", response_model=SalidaPrediccion)
def predecir(entrada: EntradaPrediccion, request: Request):
    modelo = request.app.state.modelo
    try:
        # Mismo orden de columnas que en el entrenamiento.
        columnas = list(modelo.feature_names_in_)
        X = pd.DataFrame([entrada.model_dump()])[columnas]
        valor = float(modelo.predict(X)[0])
    except Exception:
        logger.exception("Fallo al predecir")
        raise HTTPException(status_code=500, detail="Error interno al predecir")
    return SalidaPrediccion(
        prediccion=round(valor, 2),
        descripcion="Progresión estimada de la diabetes a 1 año",
    )
