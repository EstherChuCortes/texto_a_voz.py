'''Programa en python que al proporcionarle una url de un 
artiulo a convertir para luego manegar la conversacion de texto a voz.
Utiliza la biblioteca gTTS (google Text-to-speech) para convertir
el texto de una archivo en voz, nltk, newpaper3k'''
'''Este programa descarga y analiza un artículo de una URL utilizando la biblioteca 
newspaper3k. Luego, utiliza la biblioteca nltk para dividir el artículo en oraciones y 
la biblioteca gTTS para convertir cada oración en voz. Finalmente, reproduce cada oración 
convertida en voz utilizando la biblioteca playsound'''

import newspaper
import nltk
from gtts import gTTS
from playsound import playsound
import os

# Obtén la URL del artículo que deseas convertir a voz
url = "https://www.elmundo.es/espana.html"

# Descarga y analiza el artículo utilizando newspaper3k
article = newspaper.Article(url)
article.download()
article.parse()

# Utiliza nltk para dividir el artículo en oraciones
nltk.download('punkt')
sentences = nltk.sent_tokenize(article.text)

# Utiliza gTTS para convertir cada oración en voz y reproducirla
for sentence in sentences:
    # Crea un objeto gTTS para la oración actual
    tts = gTTS(text=sentence, lang='es')
    
    # Guarda el archivo de audio generado en un archivo temporal
    tts.save("temp.mp3")
    
    # Reproduce el archivo de audio utilizando la biblioteca playsound
    playsound("temp.mp3")

# Elimina el archivo temporal
os.remove("temp.mp3")