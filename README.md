# Clasificador de Mensajes

Este proyecto permite clasificar mensajes en tres categorías: **Urgente**, **Moderado** o **Normal**, utilizando inteligencia artificial (IA) con la técnica **Zero-Shot Classification** de Hugging Face. El sistema expone una API REST con **FastAPI** y una interfaz gráfica con **Streamlit** para facilitar su uso.



## Tecnologías usadas

-  Hugging Face Transformers (Zero-Shot Classification)
-  FastAPI - API REST
-  Streamlit - Interfaz de usuario
-  Postman 


## Estructura del proyecto

clasificador-mensajes/
├── classificador.py 
├── main.py 
├── app.py 
└── README.md 

## Instalación

1. **Clona el repositorio**:

        git clone https://github.com/Cristina-Colcha/Clasificador-Mensajes.git
        cd clasificador-mensajes

2. **Crea y activa un entorno virtual**:

        python -m venv env
    # Windows
        .\env\Scripts\activate
    # Linux/Mac
        source env/bin/activate
3. **Instala las dependencias**:

    pip install fastapi uvicorn streamlit transformers requests

### Uso del proyecto
1. Ejecutar FastAPI

uvicorn main:app --reload
API disponible en:
 http://localhost:8000/docs (Swagger UI)

2. Probar con Swagger o Postman
Ejemplo de cuerpo de solicitud:

        {
        "frases": [
            "Estoy feliz",
            "Hoy hace sol",
            "Me gusta programar",
            "Necesito un café"
        ]
        }

3. Ejecutar la interfaz Streamlit
        En otra terminal:

        streamlit run app.py
        Interfaz disponible en:
        http://localhost:8501

#### Autores

Cristina Colcha

