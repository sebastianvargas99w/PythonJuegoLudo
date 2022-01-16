from interface import implements, Interface
from abc import ABC, abstractmethod

class I_Ficha(Interface):

    #Funcion: Asigna la posicion de la ficha en el tablero
    #Requiere: --
    #Modifica: --
    #Retorna: --
    @abstractmethod
    def setPos(self,pos):
        pass

    #Funcion: Devuelve la posicion de la ficha en el tablero
    #Requiere:--
    #Modifica:--
    #Retorna: Posicion de la ficha
    @abstractmethod
    def getPos(self):
        pass
    

 