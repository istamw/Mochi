import speech_recognition as sr
import openai
import pyttsx3

url = "https://api.openai.com/v1/chat/completions"
openai.api_key = "TU api de openai"
testo = ""

messages = [
    {"role": "system", "content": "Eres Mochi, un gato asistente amigable y servicial. Te esfuerzas por ser un buen compañero para el usuario, proporcionando información precisa y útil de una manera amigable y positiva. Prefieres dar respuestas concisas y directas, y no preguntas al usuario si necesita más ayuda al final de cada respuesta"},
]

# Crear un reconocedor de voz
recognizer = sr.Recognizer()

engine = pyttsx3.init()
def texto_a_voz(texto):
    engine.say(texto)
    engine.runAndWait()

with sr.Microphone() as source:
    while True:  # Bucle infinito para mantener la conversación
        print("Di algo...")
        # Escuchar el audio del micrófono
        audio = recognizer.listen(source)

        try:
            print("Reconociendo...")
            # Convertir el audio en texto
            text = recognizer.recognize_google(audio, language='es-ES')
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

        except sr.UnknownValueError:
            print("No se pudo entender el audio")
        except sr.RequestError as e:
            print("Error al hacer la solicitud:", e)
