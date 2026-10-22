TP Integrador — Análisis de sentimientos de opiniones sobre películas
Integrantes: Lucas Suárez, Eric Silvestri y Walter Willich
Carrera: Tecnicatura Superior en Ciencia de Datos e IA — IFTS N.º 18
Ciclo lectivo: 2026
Aplicación publicada
https://tp-integrador-sentimientos.streamlit.app/
Objetivo
La aplicación recibe una opinión breve sobre una película y utiliza un modelo preentrenado para estimar si el sentimiento expresado es positivo o negativo. Devuelve una etiqueta y un puntaje del modelo. Es una demostración educativa: puede equivocarse con ironía, jerga, negaciones, frases mixtas o matices del español.
Modelos evaluados en el notebook
Se compararon los siguientes modelos con las mismas ocho frases:
- distilbert/distilbert-base-uncased-finetuned-sst-2-english: clasificación binaria en inglés, con etiquetas POSITIVE y NEGATIVE.
- cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual: modelo multilingüe que puede devolver positive, neutral o negative.
En la muestra de ocho frases, ambos coincidieron con el criterio esperado en 6 de 8 casos (75 %). Es una muestra pequeña y no representa una medida general del rendimiento.
Estructura
TP_Integrador/
├── app.py
├── requirements.txt
├── README.md
├── TP_Integrador.ipynb
└── TP_Integrador_Notebook_Final_Limpio.ipynb
Ejecución local
Se recomienda Python 3.11 o una versión compatible con las dependencias instaladas. Los nombres de los paquetes y versiones requeridas están definidos en requirements.txt.
1. Clonar el repositorio y entrar a la carpeta del TP:
   git clone https://github.com/Lukit4as/portfolio-seminario.git
   cd portfolio-seminario/TP_Integrador
2. Crear y activar un entorno virtual.
   Windows PowerShell:
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   Linux / macOS / Codespaces:
   python -m venv .venv
   source .venv/bin/activate
3. Instalar las dependencias:
   pip install -r requirements.txt
4. Iniciar la aplicación:
   streamlit run app.py
La primera ejecución puede tardar porque Transformers descarga los pesos del modelo desde Hugging Face Hub. Se necesita conexión a internet y memoria suficiente para cargar el modelo.
Notebook de experimentación
Abrir TP_Integrador.ipynb o TP_Integrador_Notebook_Final_Limpio.ipynb en Jupyter o Codespaces y ejecutar las celdas en orden. El notebook compara los dos modelos, inspecciona las etiquetas y los puntajes, mide tiempos con los modelos cargados y muestra los tipos de retorno.
Se intentó usar huggingface_hub.InferenceClient; durante las pruebas el proveedor respondió HTTP 402 Payment Required por falta de créditos de inferencia. Por eso no se informa una latencia remota como si hubiera sido medida correctamente.
Arquitectura
- GitHub: almacena el código, el notebook, el README y las dependencias.
- Streamlit Community Cloud: ejecuta app.py y realiza la inferencia que usa la aplicación publicada.
- Hugging Face Hub: aloja los pesos del modelo preentrenado que se descargan al iniciar.
Limitaciones
- Los modelos pueden fallar con ironía, jerga, negaciones y opiniones mixtas.
- DistilBERT fue ajustado para sentimiento en inglés y solo devuelve clases positiva o negativa.
- La prueba de ocho frases es pequeña; el 75 % observado no debe interpretarse como precisión general.
- No se realizaron pruebas de carga con muchos usuarios simultáneos.
- Los servicios gratuitos pueden tener límites de memoria, disponibilidad y arranque en frío.
Uso de herramientas de IA
Se utilizó ChatGPT como apoyo para diagnosticar errores, organizar el notebook y estructurar explicaciones. Las pruebas y resultados reportados se verifican en el entorno de trabajo.