# Clase 11 — Publicación de modelos en Hugging Face

## Objetivo

Publicar en el Hub de Hugging Face cuatro modelos entrenados con distintas bibliotecas (scikit-learn, PyTorch, Keras y Transformers) y analizar qué archivos guarda cada formato, cuáles necesita quien solo quiere usar el modelo y cuáles sirven para reproducirlo.

## Contenido de la carpeta

| Archivo | Descripción |
|---|---|
| [Respuestas clase 11.txt](<Respuestas clase 11.txt>) | Respuestas a las nueve preguntas de la actividad |

Las respuestas abordan los siguientes temas:

1. Forma de carga de los archivos al Hub.
2. Etiquetas de la Model card y el bloque de metadatos del `README.md`.
3. Archivo del modelo entrenado en cada repositorio.
4. Diferencias entre los `config.json` de PyTorch y de Transformers.
5. Por qué PyTorch necesita `modelo.py` y Keras no.
6. Uso de los modelos con `InferenceClient`.
7. Botón *Use this model* del Hub.
8. Requisitos para utilizar el modelo de PyTorch desde otro código.
9. Alternativas al Hub para compartir modelos.

## Requisitos

- Cuenta en Hugging Face
- Modelos exportados en la Clase 10

## Cómo reproducirlo

1. Crear un repositorio de modelo en el Hub para cada biblioteca.
2. Cargar los archivos del modelo, su `README.md` con los metadatos y las instrucciones de uso.
3. Revisar la pestaña *Model card* y el botón *Use this model* de cada repositorio.
4. Responder las preguntas de la actividad.

## Resultado esperado

Cuatro repositorios publicados en el Hub, cada uno con el modelo, su documentación y un script de predicción, junto con el archivo de respuestas que compara los formatos de exportación.
