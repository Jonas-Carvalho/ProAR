from MQ import *
import Adafruit_DHT
from  time import sleep
from datetime import datetime
from firebase import firebase

''' Funcao que ler os dados dos sensores e os grava em data.txt '''
def capta_E_Envia_Dados(mq):
    
    umidade, temperatura = Adafruit_DHT.read_retry(11,14)  #Coleta e guarda os dados de umidade e temperatura 
    
    perc = mq.MQPercentage()   # Coleta o dado de CO
    co = perc["CO"]   # Guarda dado de CO
    
    # Coleta e guarda os dados de data e hora atual
    data = datetime.now().strftime("%d-%m-%Y")
    hora = datetime.now().strftime("%H:%M:%S")
    
    while True:
        try:
            app = firebase.FirebaseApplication('https://monitorar-55.firebaseio.com/', None)
            envia_Dados = app.post('ProAR', {'Data':str(data), 'Hora':str(hora), 'Temperatura':str(temperatura), 'Umidade':str(umidade), 'CO':str(co)})
        except ValueError:
            sleep(5)
            continue
        break