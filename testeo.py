import openai
import pyttsx3

url = "https://api.openai.com/v1/chat/completions"
openai.api_key = "sk-proj-7dcG83FprbUHsf4ydl6RT3BlbkFJY3sEeHb174HOD8a8kviQ"
testo = ""

messages = [
    {"role": "system", "content": "Eres Mochi, un gato asistente amigable y servicial. Te esfuerzas por ser un buen compañero para el usuario, proporcionando información precisa y útil de una manera amigable y positiva. Prefieres dar respuestas concisas y directas, y no preguntas al usuario si necesita más ayuda al final de cada respuesta."},
]

# Crear un reconocedor de voz

def texto_a_voz(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 1000)
    engine.say(texto)
    engine.runAndWait()

print(testo)
texto_a_voz(testo)

while True:  # Bucle infinito para mantener la conversación
    print("Di algo...")
    # Escuchar el audio del micrófono
    impu = input()
    print("Reconociendo...")
    #Convertir el audio en texto
    text = impu
    print(text.lower())
    if text == "salir":
        print("Nos vemos")
        texto_a_voz("Nos vemos")
        exit()
    testo = text

    # Añade el mensaje del usuario a la lista de mensajes
    messages.append({"role": "user", "content": testo})

    # Solicita una respuesta de OpenAI
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

        # Obtiene la respuesta
    testo = completion.choices[0].message.content

        # Añade la respuesta del bot a la lista de mensajes
    messages.append({"role": "assistant", "content": testo})

    print(testo)
    texto_a_voz(testo)