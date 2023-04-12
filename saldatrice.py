class saldatrice:
    # Nome della saldatrice
    name = ''
    # Lista variabili per la connessione
    ip = 0
    port = 0
    number = 0
    # Temperature perheating
    temp_preHeating1 = 0
    temp_preHeating2 = 0
    temp_preHeating3 = 0
    temp_bath = 0
    RPM_mainPump = 0
    RPM_chipPump = 0
    in_sensor = False
    # Numero dei carrelli
    numCarr = 10
    # Contatore carrelli
    carrCounter = []

    # Inzializzazione
    def __init__(self, Name):
        self.setName(Name)
        # Inizializzo i contatori dei carrelli a 0
        #for x in range(0, self.numCarr - 1, 1):
        #    self.carrCounter[x] = 0;

    # Metodo per impostare il nome
    def setName(self, NAME):
        self.name = NAME

    # Metodo per leggere il nome
    def getName(self):
        return self.name

    # Metodo per impostare l'indirizzo IP
    def setIP(self, IP):
        self.ip = IP
    
    # Metodo per leggere l'indirizzo IP
    def getIP(self):
        return self.ip

    # Metodo per impostare la porta di comunicazione
    def setPort(self, PORT):
        self.port = PORT

    # Metodo per leggere la porta di comunicazione
    def getPort(self):
        return self.port

    # Metodo per impostare il numero della saldatrice
    def setNumber(self, N):
        self.number = N

    # Metodo per leggere il numero della saldatrice
    def getNumber(self):
        return self.number
    
    # Metodo per impostare la temperatura della resistenza 1
    def setTempPreH1(self, temp):
        self.temp_preHeating1 = temp

    # Metodo per leggere la temperatura della resistenza 1
    def getTempPreH1(self):
        return self.temp_preHeating1

    # Metodo per impostare la temperatura della resistenza 2
    def setTempPreH2(self, temp):
        self.temp_preHeating2 = temp

    # Metodo per leggere la temperatura della resistenza 2
    def getTempPreH2(self):
        return self.temp_preHeating2

    # Metodo per impostare la temperatura della resistenza 3
    def setTempPreH3(self, temp):
        self.temp_preHeating3 = temp

    # Metodo per leggere la temperatura della resistenza 3
    def getTempPreH3(self):
        return self.temp_preHeating3

    # Metodo per impostare la temperatura della resistenza 3
    def setTempBath(self, temp):
        self.temp_bath = temp

    # Metodo per leggere la temperatura della resistenza 3
    def getTempBath(self):
        return self.temp_bath

    # Metodo per impostare gli RPM della pompa principale
    def setRPMmainPump(self, value):
        self.PRM_mainPump = value

    # Metodo per leggere gli RPM della pompa principale
    def getRPMmainPump(self):
        return self.PRM_mainPump

    # Metodo per impostare gli RPM della pompa chip
    def setRPMchipPump(self, value):
        self.RPM_chipPump = value

    # Metodo per leggere gli RPM della pompa chip
    def getRPMchipPump(self):
        return self.RPM_chipPump

    # Metodo per settare il sensore in ingresso
    def SetInSensor(self):
        self.in_sensor = True
        
    # Metodo per resettare il sensore in ingresso
    def ClrInSensor(self):
        self.in_sensor = False

    # Metodo che restituisce lo stato del sensore in ingresso
    def getInSensor(self):
        return self.in_sensor
