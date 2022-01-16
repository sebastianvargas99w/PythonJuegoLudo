from abc import ABC, abstractmethod
from interface import implements, Interface

class I_Casilla(Interface):

    #Debido a que python no usa tipos fuertes la lista fichas se puede usar para contener
    #todo tipo de objetos si se necesitara.
    
    #Ubica una ficha en la casilla.
    @abstractmethod
    def agregarFicha(self,ficha,controlador):
        raise NotImplementedError

    #Saca a la ultima ficha que ingreso, otro metodo la movera despues.
    @abstractmethod
    def sacarFicha(self):
        raise NotImplementedError
        
    #Devuelve las coordenadas de la casilla como si fuera una matriz.
    @abstractmethod
    def obtenerPosicion(self):
        raise NotImplementedError