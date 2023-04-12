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

    # Inzializzazione
    def __init__(self, Name):
        self.setName(Name)

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

    # Metodo per impostare gli RPM della pompa principale
    def setRPMmainPump(self, RPM):
        self.PRM_mainPump = RPM

    # Metodo per leggere gli RPM della pompa principale
    def getPRMmainPump(self):
        return self.PRM_mainPump

    # Metodo per impostare gli RPM della pompa chip
    def setPRMchipPump(self, RPM):
        self.RPMM_chipPump = RPM

    # Metodo per leggere gli RPM della pompa chip
    def getRPMchipPump(self):
        return self.RPM_chipPump
