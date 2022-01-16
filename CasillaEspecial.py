from Casilla import Casilla
from abc import ABC, abstractmethod

class CasillaEspecial(Casilla):

    especial = True

    #Obliga a las clases a tener un atributo de nombre color y que sea un string.
    @property
    @abstractmethod
    def color(self) -> str:
        raise NotImplementedError

    #Obliga a las clases a tener un atributo de nombre tipo y que sea un string.
    @property
    @abstractmethod
    def tipo(self) -> str:
        raise NotImplementedError

    #Obliga a las clases a tener un metodo que defina el comportamiento de la casilla
    @abstractmethod
    def aplicarComportamiento(self):
        raise NotImplementedError

    def obtenerColor(self):
        return self.color