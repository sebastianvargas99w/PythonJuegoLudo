import pickle
from Jugador import Jugador
from Ficha import Ficha
import copy
from I_GestorPartidas import I_GestorPartidas
from interface import implements, Interface

#Se encarga de guardar y cargar partidas
class GestorPartidas(implements(I_GestorPartidas)):

    #Constructor de GestorPartida.
    def __init__(self):
        pass

    #Función: Lee el archivo binario y devuelve los objetos leidos para retomar una partida.
    #Requiere: el nombre de un archivo que sea generado con el metodo guardar de este juego
    #Modifica:No modifica ningun parametro
    #Retorna: modeloTablero,jugadores,jugadorActual y dado
    def cargar(self,archivo):
        partida = open( archivo, "rb" )
        #orden en que estan guardadas las variables
        #tablero,jugadores,jugadorActual,dado
        modeloTablero = pickle.load(partida)
        jugadores = pickle.load(partida)
        jugadorActual = pickle.load(partida)
        dado = pickle.load(partida)
        partida.close()
        return modeloTablero,jugadores,jugadorActual,dado
        
    #Función:Guarda la informacion necesaria en binario para retomar la partida luego.
    #Requiere: Tablero,jugador actual y dado se pueda guardar con pikle
    #Modifica: No modifica ningun parametro
    #Retorna: No retorna ningun parametro
    def guardar(self,nombreArchivo,tablero,jugadores,jugadorActual,dado = 0):

        archivo = open(nombreArchivo,"wb")
        nuevosJugadores = []
        
        #copia la clase jugadores para esta implementacion en particular porque hay un objeto que pikle no permite guardar
        for contador in range (0, len(jugadores)):
            nuevosJugadores.append(copy.copy(jugadores[contador]))
        #crea una lista con las fichas de cada jugador sin el objeto que no se puede guardar
        for contador in range(0,len(nuevosJugadores)):
            auxiliarFichas = []
            for iteradorFicha in range (0, len(nuevosJugadores[contador].fichas)):
                auxiliarFichas.append(  Ficha(jugadores[contador].fichas[iteradorFicha].posicion,jugadores[contador].fichas[iteradorFicha].color,jugadores[contador].fichas[iteradorFicha].base,None,None,jugadores[contador].fichas[iteradorFicha].botonVista,None)    )
            nuevosJugadores[contador].fichas = auxiliarFichas
            nuevosJugadores[contador].casillaInicial = None
        
        #guardar los objetos
        pickle.dump(tablero, archivo)
        pickle.dump(nuevosJugadores, archivo)
        pickle.dump(jugadorActual, archivo)
        pickle.dump(dado, archivo)
        archivo.close()