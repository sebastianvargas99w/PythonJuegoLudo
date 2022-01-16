from abc import ABC, abstractmethod
from interface import implements, Interface

#Obliga a las clases a tener un metodo que defina el comportamiento de la casilla
class I_GestorPartidas(Interface):
    
    #Función: Lee el archivo binario y devuelve los objetos leidos para retomar una partida.
    #Requiere: el nombre de un archivo que sea generado con el metodo guardar de este juego
    #Modifica:No modifica ningun parametro
    #Retorna: modeloTablero,jugadores,jugadorActual y dado
    @abstractmethod
    def cargar(self,archivo):
        raise NotImplementedError
        
    #Función:Guarda la informacion necesaria en binario para retomar la partida luego.
    #Requiere: Tablero,jugador actual y dado se pueda guardar con pikle
    #Modifica: No modifica ningun parametro
    #Retorna: No retorna ningun parametro
    @abstractmethod
    def guardar(self,nombreArchivo,tablero,jugadores,jugadorActual,dado = 0):
        raise NotImplementedError
