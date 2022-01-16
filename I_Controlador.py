from abc import ABC, abstractmethod
from interface import implements, Interface

class I_Controlador(Interface):

    #Funcion: inicializa los jugadores 
    #Requiere: lista de jugadores
    #Modifica: Jugadores
    #Retorna: Jugadores inicializados
    @abstractmethod
    def iniciarJugadores(self,jugadores):
        pass

    #Funcion: Pone el color de cada jugador
    #Requiere: 
    #Modifica: Jugador
    #Retorna: -
    @abstractmethod
    def escogerColores(self):
        pass

    #Funcion: Mueve fichas en el tablero
    #Requiere: jugador, ficha,tablero
    #Modifica: Posicion de la ficha
    #Retorna: -
    @abstractmethod
    def moverFicha (self,jugador,ficha):
        pass

    #Funcion: Cambia de turno para seguir el orden del juego
    #Requiere: -
    #Modifica: jugador en turno
    #Retorna: -
    @abstractmethod
    def cambiarTurno(self):
        pass

    #Funcion: Tira el dado para jugar
    #Requiere: -
    #Modifica: -
    #Retorna: dado
    @abstractmethod
    def tirarDado(self):
        pass

    #Funcion: Escoge el primer jugador de la partida
    #Requiere: label para informar
    #Modifica: turnos de jugadores
    #Retorna: -
    @abstractmethod
    def escogerPrimero (self, labT):
        pass

    #Funcion: Carga una partida guardada
    #Requiere: archivo
    #Modifica: -
    #Retorna: -
    @abstractmethod
    def cargar(self, archivo):
         pass

    #Funcion: Guarda la partida actual
    #Requiere: archivo
    #Modifica: archivo
    #Retorna: -
    @abstractmethod
    def guardar(self, archivo):
        pass

    #Funcion: Reinicia la lista de jugadores
    #Requiere: --
    #Modifica: --
    #Retorna: --
    @abstractmethod
    def resetJugadores(self):
        pass

    #Funcion: Determina si un jugador termino o gano la partida 
    #Requiere: --
    #Modifica:--
    #Retorna: --
    @abstractmethod
    def terminado(self, par1=None, par2 = None, j = None):
        pass

    #Funcion: Obtiene lista de jugadores
    #Requiere: --
    #Modifica: --
    #Retorna: --
    @abstractmethod
    def obtenerJugadores(self):
        pass


