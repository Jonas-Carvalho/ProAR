from funcoes import * # Importa principais funcoes do arquivo funcoes.py

mq = MQ() # Configura e inicia o sensor de CO 

while True:
    try:
        print('data: ' + str(datetime.now().strftime("%H:%M:%S")) + ' hora: ' + str(datetime.now().strftime("%d-%m-%Y")) + ' - ENVIANDO dados')
        capta_E_Envia_Dados(mq)
        print('data: ' + str(datetime.now().strftime("%H:%M:%S")) + ' hora: ' + str(datetime.now().strftime("%d-%m-%Y")) + ' - OK')
        sleep(600)
    except:
        sleep(10)
        continue