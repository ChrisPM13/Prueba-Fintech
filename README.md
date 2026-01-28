#### **Instrucciones para correr Fintech Credit API**



Clonar el repositorio:

git clone https://github.com/tu\_usuario/fintech-api.git

cd fintech-api



Crear y activar entorno virtual .venv:

Windows:

python -m venv .venv

.venv\\Scripts\\activate



Linux/macOS:

python3 -m venv .venv

source .venv/bin/activate



Instalar dependencias:

pip install -r requirements.txt



Levantar la API:

uvicorn app.main:app --reload



La API estará disponible en: http://127.0.0.1:8000



#### **Flujo de uso end-to-end:**



Crear solicitud de crédito: POST /applications con JSON de datos del cliente



Consultar estado de la solicitud: GET /applications/{application\_id}



Subir comprobante de domicilio: POST /applications/{application\_id}/documents (solo PDF, JPG o PNG)



Opcional: obtener score aleatorio con GET /scorecredito



#### **Nota**



Todos los datos se guardan en SQLite (fintech.db)

El mock de IA devuelve los datos ingresados para simular la extracción correcta de información







### 1\. Descripción del proyecto



Este proyecto es una prueba técnica para una Fintech de crédito al consumo

El objetivo es crear un sistema backend que permita:



Procesar solicitudes de crédito digital



Extraer información de comprobantes de domicilio (simulado con IA mock)



Evaluar reglas de aprobación crediticia



Guardar la información de manera persistente



Exponer el flujo de decisión de forma explicable



El proyecto está implementado con:



Python 3.11+



FastAPI como framework backend



SQLAlchemy para ORM y persistencia en SQLite (para pruebas)



IA (mock) para extracción de información de documentos - mock simulación de IA



### 2\. Decisiones técnicas



Framework y lenguaje



FastAPI: fácil de usar, permite endpoints asíncronos y documentación automática (Swagger UI)



Python: rápido para prototipado y manejo de IA



Persistencia de datos



SQLite para pruebas locales, tablas applications, decisions y documents



En producción se recomienda PostgreSQL o MySQL



### 3\. Motor de reglas



Separado en rule\_engine.py para permitir escalabilidad y cambios



Reglas implementadas:



Score de crédito entre 500 y 900



Ingreso mínimo > 8000



Fácil de extender con nuevas reglas (edad, dirección válida, lista negra, antigüedad bancaria, etc.)



### 4\. IA para documentos



Actualmente mock (ai\_service.py) que devuelve nombre, dirección y fecha. En este caso se uso el mock por ser prueba



En producción se puede integrar con OCR (Tesseract, Azure Form Recognizer, AWS Textract) y normalización de direcciones con LLM



### 5\. Explicabilidad



Cada solicitud incluye un explanation que describe el resultado de cada regla evaluada, cumpliendo con trazabilidad y requisitos regulatorios.





#### Para producción:



Uso de IA real 

Extensibilidad para otros productos financieros

Agregar una mejor trazabilidad y control exponiendo endpoints adicionales

Optimizar validando datos con mayor profundidad

Cambiar a una base datos robusta

Autenticación de usuarios





