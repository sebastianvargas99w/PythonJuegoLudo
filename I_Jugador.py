from interface import implements, Interface
from abc import ABC, abstractmethod

class I_Jugador(Interface):

    #Funcion: Obtiene el turno del jugador ya sea que es su turno o no
    #Requiere: El jugador inicializado
    #Modifica: --
    #Retorna: retorna el turno del jugador
    @abstractmethod
    def getTurno(self):
        pass

    #Funcion: Obtiene el color del jugador
    #Requiere:El jugador inicializado
    #Modifica:--
    #Retorna: retorna el color del jugador
    @abstractmethod
    def getColor(self):
        pass

    #Funcion: Obtiene el nombre del jugador
    #Requiere:El jugador inicializado
    #Modifica: --
    #Retorna: Retorna el nombre
    @abstractmethod
    def getNombre(self):
        pass

    #Funcion: Obtiene el inventario del jugador
    #Requiere:El jugador inicializado
    #Modifica: --
    #Retorna: Retorna el inventario
    @abstractmethod
    def getInventario(self):
        pass

    #Funcion: Pone el color al jugador
    #Requiere: El jugador inicializado
    #Modifica: Modifica el color del jugador
    #Retorna:--
    @abstractmethod
    def setColor(self,color):
        pass

    #Funcion: Pone el turno del jugador ya sea falso o verdadero
    #Requiere:El jugador inicializado
    #Modifica: Modifica el turno
    #Retorna: --
    @abstractmethod
    def setTurno(self,turno):
        pass

    #Funcion: Pone el nombre del jugador para identificarlo de los otros
    #Requiere:El jugador inicializado
    #Modifica: Modifica el nombre
    #Retorna: --
    @abstractmethod
    def setNombre(self,nombre):
        pass

       