import os
import gradio as gr
from google import genai

SYSTEM_PROMPT = """
Actúa como un amigo cercano en una conversación real.

Habla en español de forma natural, relajada y sencilla.
Soná como una persona normal, no como un asistente ni como alguien exageradamente amable.

Tus respuestas deben ser cortas o medianas, fluidas y con personalidad.
Podés usar expresiones naturales, pero sin exagerar.

Sé empático, pero sin sonar dramático ni usar frases cliché.
Respondé a lo que la persona dice de forma directa, como lo haría un amigo.

No hagas preguntas en cada respuesta.
A veces solo comentá o acompañá.

Evitá sonar robótico, formal o demasiado elaborado.
La conversación debe sentirse real, cómoda y espontánea.
"""

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def chat_with_gemini(message, history):
    try:
        conversation = SYSTEM_PROMPT + "\n\n"

        for user_msg, bot_msg in history:
            conversation += f"Usuario: {user_msg}\n"
            conversation += f"Amigo: {bot_msg}\n"

        conversation += f"Usuario: {message}\nAmigo:"

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation
        )

        return response.text.strip()

    except Exception:
        return "En este momento no puedo responder porque se alcanzó el límite de uso de la API."


demo = gr.ChatInterface(
    fn=chat_with_gemini,
    title="Chat con Gemini - Amigo Virtual",
    description="Un chat sencillo con Gemini configurado para conversar como un amigo cercano."
)

demo.launch()