import webbrowser
import speech_recognition as sr
import pyttsx3 as voz
from datetime import datetime

voice=voz.init()
voices=voice.getProperty('voices')
voice.setProperty('voice',voices[0].id)
voice.setProperty('rate',140)

def say(text):
    voice.say(text)
    voice.runAndWait()

print('¡Hola, soy Juanita! :)')
say('Hola, soy Juanita. Dime algo...')

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Escuchando... ')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='es-MX')
            print('Creo que has dicho: {}'.format(text))
            say(text)
            if 'Amazon' in text:
                webbrowser.open('https://amazon.com.mx')
                say(f'Abriendo Amazon')

            if 'Google' in text:
                webbrowser.open('https://google.com.mx')
                say(f'Abriendo Google')

            if 'YouTube' in text:
                webbrowser.open('https://youtube.com')
                say(f'Abriendo YouTube')

            if 'hora' in text:
                    time=datetime.now().strftime('%H:%M')
                    print(time)
                    say(f'Son las {time}')

            if 'gracias' in text:
                print('De nada')
                say('De nada')

            if 'adiós' in text:
                print('Adiós loco')
                say('Adiós loco')
                break

        except:
            print('No te entendí... ')
            say('No te entendí')