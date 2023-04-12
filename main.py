#!/usr/bin/python

# Importo le librerie necessarie
from socket import *
import time
import calendar
import saldatrice

# 03-AXXXBXXXCXXXDXXXEXXXFXXX
# A -> Preheating 1
# B -> Preheating 2
# C -> Preheating 3
# D -> Main Pump RPM
# E -> Chip Pump RPM
# F -> Conveyor Speed
def infoData(data_in):
    # Tolgo la parte iniziale della stringa ( il codice -> 03- )
    data_in = data_in[3:]
    # Inizializzo il puntatore della potenza degli interi
    ptr = 0
    int_cr = 0
    # Ciclo la stringa per la decodifica
    for i in range(len(data_in), 0, -1):
        # Estraggo il carattere
        cr = data_in[i-1:i]
        # Eseguo la conversione a int
        try:
            int_cr += int(cr) * pow(10,ptr)
            ptr += 1
        except ValueError:
            # Se è una lettera questa è la lettere che mi indica che parametro è
            param = cr
            if param == 'A':
                pass
            elif param == 'B':
                pass
            elif param == 'C':
                pass
            #
            elif param == 'D':
                pass
            # E RPM pompa Main
            elif param == 'E':
                pass
            # F RPM pompa Chip
            elif param == 'F':
                pass
            else:
                print("Parametro in ingresso sconosciuto")
            int_cr = 0
            ptr = 0

###########################################
#   MAIN                                  #
###########################################
# Array di saldatrici
sald = 0
number = 0

# Inizio programma
print("Lettura files...")

# Tento la lettura dei file di configurazione
try:
    file = open("netconfig.ini", "r")
    print("Caricamento saldatrice")
    # Ciclo il file di configurazione
    for x in file:
        # Tolgo il \n dalla stringa
        x = x.translate(str.maketrans('','','\n'))

        #Controllo di non essere alla fine
        if x == '__123end321__':
            print("Lettura eseguita")
            break
        
        # Nuova saldatrice
        print("Saldatrice: " + x)
        # Creo una nuova istanza
        sald = saldatrice.saldatrice(x)

        # Leggo l'indirizzo IP
        x = file.readline()
        # Tolgo il \n dalla stringa
        x = x.translate(str.maketrans('','','\n'))
        print("Indirizzo IP: " + x)
        # Salvo nella classe
        sald.setIP(x)

        # Leggo la porta
        x = file.readline()
        # Tolgo il \n dalla stringa
        x = x.translate(str.maketrans('','','\n'))
        print("Porta: " + x)
        # Salvo nella classe
        sald.setPort(int(x))

        # Imposto il numero
        sald.setNumber(number)

        # Incremento il contatore
        number = number + 1
    # Chiudo il file
    file.close()
except:
    print("Impossibile leggere i file di configurazione")

rec_data = '03-A100B200C300D400E500F600'
infoData(rec_data)

# Mi connetto
adress = ( sald.getIP(), sald.getPort() )
sock = socket(AF_INET, SOCK_DGRAM)
sock.settimeout(1)

# Sincronizzo data/ora
print("Sincronizzazione data/ora...")
current_GMT = time.gmtime()
time_stamp = calendar.timegm(current_GMT)
# Compongo il dato
timeSync = "01-" + str(time_stamp)
print(timeSync)
timeSync = bytes(timeSync ,'utf-8')
print(timeSync)
# Lo invio
sock.sendto(timeSync, adress)
rec_data, addr = sock.recvfrom(2048)
print ("Data recived", rec_data, " ", addr)
# Controllo la corretta ricezione
rec_data = rec_data.decode("utf-8")
if rec_data == '01-AckOK':
    print("Sincronizzazione eseguita")
else:
    print("Errore nella sincronizzazione")

cnt = 0

while True:
    if True:
        # Leggo il buffer
        rec_data, addr = sock.recvfrom(2048)
        print ("Data recived", rec_data, " ", addr)
        # Decodifico il dato
        rec_data = rec_data.decode('utf-8')
        print(rec_data)
        #Prendo le prime due cifre per la decodifica
        sub_rec_data = rec_data[:2]
        # Codice 02, richiesta nuovo profilo
        # 02-NNNOOOO
        if sub_rec_data == '02':
            sendProfile()
        # Codice 03, invio dati parametrici forno (non di stato)
        # 03-P1TTTP2TTTP3TTTBTTTCVVVMRRRCRRR
        elif sub_rec_data == '03':
            infoData()
    else:
        continue

def sendProfile(self):
    # Ricavo il numero del profilo
    profile_num = rec_data[3:6]
    # Ricavo il codice operatore
    operator_num = rec_data[6:]
    # Apro il file del profilo
    file_path = "profili/" + str(profile_num) + ".ini"
    profile = open(file_path, 'r')
    string_to_send = "02-"
    # Compongo la stringa
    for x in profile:
        # Tolgo il \n dalla stringa
        x = x.translate(str.maketrans('','','\n'))
        string_to_send += "P" + x
    # Chiudo il file
    profile.close()
    # Scerivo il log
    string_to_log = "["
    string_to_log += time.strftime("%Y-%m-%d %H:%M:%S")
    string_to_log += "] New request: profile #"
    string_to_log += str(profile_num)
    string_to_log += ", operator #"
    string_to_log += str(operator_num)
    string_to_log += " ARG: "
    string_to_log += string_to_send
    # Compongo il dato
    string_to_send = bytes(string_to_send ,'utf-8')
    # Lo invio
    sock.sendto(string_to_send, adress)
    rec_data, addr = sock.recvfrom(2048)
    print ("Data recived", rec_data, " ", addr)
    # Controllo la corretta ricezione
    rec_data = rec_data.decode("utf-8")
    print(rec_data)
    if rec_data == '02-AckOK':
        print("Sincronizzazione eseguita")
    else:
        print("Errore nella sincronizzazione")
    # Salvo anche nel log
    string_to_log += " Response: "
    string_to_log += rec_data
    string_to_log += "\n"
    # Apro il log
    profile_log = open("log/profilesReq.log", 'a')
    # Scrivo nel log
    profile_log.write(string_to_log);
    # Chiudo il file
    profile_log.close()
