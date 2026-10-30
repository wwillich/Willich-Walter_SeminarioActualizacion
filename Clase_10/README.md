# Clase 10 — Del dataset al modelo exportado

## Objetivo

Recorrer el camino completo del entrenamiento de un modelo de regresión lineal que predice el precio de una casa a partir de sus metros cuadrados, balcón y ascensor, y guardarlo en un archivo que pueda utilizarse en otra aplicación sin volver a entrenar.

## Contenido de la carpeta

| Archivo | Descripción |
|---|---|
| [Clase_10_Notebook_Camino_Entrenamiento.ipynb](Clase_10_Notebook_Camino_Entrenamiento.ipynb) | Notebook de la clase, con el desarrollo y las actividades |

La notebook se organiza en los siguientes apartados:

1. El problema: un conjunto de 200 casas con su precio.
2. Una vuelta del camino, a mano: datos, predicción, pérdida y corrección de `w` y `b`.
3. scikit-learn: `LinearRegression`, `SGDRegressor` y el escalado de las variables de entrada.
4. PyTorch: el ciclo de entrenamiento escrito paso a paso.
5. Keras: el mismo ciclo dentro de `fit`.
6. Evaluación con casas que el modelo no vio durante el entrenamiento.
7. Qué es un modelo.
8. Exportación del modelo: `joblib` (scikit-learn), `state_dict` (PyTorch) y `.keras` (Keras).
9. Actividad sobre qué guarda cada formato, repaso y glosario.

## Requisitos

- Python 3.10 o superior
- Jupyter o VS Code con la extensión de Jupyter
- Bibliotecas: `numpy`, `pandas`, `matplotlib`, `scikit-learn`, `torch`, `keras` (con un backend instalado, por ejemplo TensorFlow) y las que instala la propia notebook en su primera celda (`skops`, `skl2onnx`, `onnx`, `onnxscript`, `onnxruntime`)

> **Nota:** la notebook está pensada para ejecutarse en Google Colab, donde estas bibliotecas ya están disponibles.

## Cómo reproducirlo

1. Abrir la notebook en Google Colab o en VS Code.
2. Ejecutar las celdas **de a una y en orden**, completando las respuestas de las celdas de predicción antes de correr el código correspondiente.
3. Al llegar al apartado 8, verificar que se generen los archivos exportados.

## Resultado esperado

Un modelo de regresión lineal entrenado con las tres bibliotecas, evaluado con datos no vistos y exportado en el formato propio de cada una.
