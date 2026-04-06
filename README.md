# Chat con Gemini desde consola

Este proyecto implementa un chat en consola utilizando Python y la API de Gemini de Google.  
El agente fue diseñado para comportarse como un amigo cercano, generando respuestas naturales, simples y conversacionales.

---

## Tecnologías utilizadas

- Python
- Gemini API (Google)
- SDK: google-genai

---

## Configuración del proyecto

### 1. Crear entorno virtual

```bash
python -m venv .venv
```

Activar el entorno:

```bash
.venv\Scripts\activate
```

---

### 2. Instalar dependencias

```bash
pip install google-genai
```

---

### 3. Configurar API Key

En PowerShell:

```powershell
$env:GEMINI_API_KEY="TU_API_KEY"
```

> Importante: No incluir la API key real en el código ni en el repositorio.

---

## Ejecución

```bash
python app.py
```

---

## Funcionalidad

- Chat interactivo desde consola  
- Interfaz web utilizando Gradio  
- Respuestas generadas por Gemini  
- Comportamiento tipo “amigo”  
- Ajuste del estilo mediante prompt engineering  

---

## Interfaz web

Además de la versión en consola, se desarrolló una interfaz web utilizando Gradio, lo que permite interactuar con el agente de forma más visual y amigable.

Para ejecutar la versión web:

```bash
python gradio_app.py
```
---

Esto levanta un servidor local accesible desde el navegador.

Nota: Debido a los límites del plan gratuito de la API, puede no responder si se alcanza el límite de solicitudes.

## Diseño del agente

El comportamiento del agente se controla mediante un prompt que define su personalidad como un “amigo cercano”.  
Se realizaron varias iteraciones para lograr un balance entre naturalidad, empatía y fluidez en la conversación.

---

## Aprendizajes

Durante el desarrollo de este proyecto se aprendió:

- Uso de APIs de inteligencia artificial generativa  
- Manejo de variables de entorno para proteger credenciales  
- Creación y uso de entornos virtuales en Python  
- Control del comportamiento de un modelo mediante prompts  

---

## Posibles mejoras

- Interfaz web (Flask o FastAPI)  
- Entrada y salida por voz  
- Memoria conversacional más avanzada  
- Personalización del estilo del agente  

---

## Autor

Hilary Madrigal Valverde