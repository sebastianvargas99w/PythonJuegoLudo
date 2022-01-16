import random
from Casilla import Casilla
from I_Jugador import I_Jugador
from interface import implements, Interface

class Jugador(implements(I_Jugador)):
    fichas=[]  
    color="" 
    base = []
    casillas=[]

    casillaInicial = 0
    botones=[]
    turno = None
    baseFichas=[]
    
    #Funcion: Constructor del jugador
    #Requiere: --
    #Modifica: Jugador
    #Retorna: Jugador
    def __init__(self,color=None,turno=None,base = None,):
        self.color=color
        self.turno = turno
        self.fichas = []
        self.base = []
        self.baseFichas=[]
        self.botones=[]
        self.casillaInicial = 0
        self.casillas = []

        
    #Funcion: Obtiene el turno del jugador ya sea que es su turno o no
    #Requiere: El jugador inicializado
    #Modifica: --
    #Retorna: retorna el turno del jugador
    def getTurno(self):
        return self.turno

    #Funcion: Obtiene el color del jugador
    #Requiere:El jugador inicializado
    #Modifica:--
    #Retorna: retorna el color del jugador
    def getColor(self):
        return self.color
    
    #Funcion: Obtiene las fichas de cada jugador
    #Requiere: El jugador inicializado, fichas inicializadas
    #Modifica: --
    #Retorna: Fichas del jugador
    def getFichas(self):
        return self.fichas
    
    #Funcion: Pone el color al jugador
    #Requiere: El jugador inicializado
    #Modifica: Modifica el color del jugador
    #Retorna:--
    def setColor(self,color):
        self.color=color

    #Funcion: Pone el turno del jugador ya sea falso o verdadero
    #Requiere:El jugador inicializado
    #Modifica: Modifica el turno
    #Retorna: --
    def setTurno(self,turno):
        self.turno=turno
        
    def getNombre(self):
        return self.color
    
    def getInventario(self):
        return self.fichas
    
    def setNombre(self,nombre):
        self.color = nombre


       

    


        
