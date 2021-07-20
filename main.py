from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

import yaml #PyYAML es un analizador y emisor YAML para Python. 

import os #Libreria para los comandos del sistema operativo.

#Importamos loggin para que no aparezca el error
#No value for search_text was available on the provided input
import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

#Importamos la libreria del TTS TextToSpeech - Texto a Voz
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate", 150)#Aplico el tempo de pronunciacion

chatbot = ChatBot(
    "Edd Computer", #Nombre del Chatbot
    trainer="chatterbot.trainers.ChatterBotCorpusTrainer", #declaramos trainer como llamada a los trainer de chatterbot, en especifico a los del Corpus trainer
    storage_adapter="chatterbot.storage.SQLStorageAdapter", #declaramos el adaptador de almacenamiento, que en este caso sera SQL
    database_url="sqlite://botData.sqlite3" #especificamos la ruta de SQLite de la base de datos del conocimiento del Chatbot
)
#chatbot.trainers("chatterbot.corpus.spanish")

trainer = ChatterBotCorpusTrainer(chatbot) #Declaramos que nuestro trainer le aplique al chatbot los trainer de Corpus
trainer.train("chatterbot.corpus.spanish") #Asignamos al trainer a usar los archivos de conocimiento del corpus
trainer.train("data/soporte2.yml") # Asignamos al trainer a usar nuestro archivo de reparacion de computadoras

os.system("cls") #limpiamos la pantalla, debido a que se muestra informacion de carga de los conocimientos de nuestro chatbot.
engine.setProperty("rate", 150)#aplicamos la velocidad de de pronunciacion
engine.say("Hola, Bienvenido a E D D Computer. Sere tu asistente en reparación de computadoras. ¿En que puedo ayudarte?")#hacemos que el chatbot nos diga un msj personalizado.
print("Hola, Bienvenido a EDD Computer. Sere tu asistente en reparación de computadoras. ¿En que puedo ayudarte?")#imprimimos el msj personalizado
engine.runAndWait()#antes de ejecutar una nueva linea de comandos, el tts debe de terminar de hablar.

while True:
        usuario = input("Cliente: >>> ").lower() #  input del usuario
        respuesta = chatbot.get_response(usuario) # buscador de respuesta de la base de datos
        engine.setProperty("rate", 135) #aplicamos la velocidad de pronunciacion
        engine.say(respuesta)#hacemos que el engine nos diga la respuesta que obtuvo de lo que le pedimos
        print("\nEdd Computer: "+str(respuesta)) #imprimimos la respuesta que nos dira el chatbot
        engine.runAndWait()#