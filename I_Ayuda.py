from abc import ABC, abstractmethod
from interface import implements, Interface

class I_Ayuda(Interface):

    #Funcion: Muestra las reglas e instrucciones del juego.
    #Requiere: --
    #Modifica: --
    #Retorna: --
    @abstractmethod
    def mostrarReglas(self):
        pass
    