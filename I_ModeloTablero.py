from abc import ABC, abstractmethod
from interface import implements, Interface

class I_ModeloTablero(Interface):

    #Funcion: Crea el tablero 
    #Requiere: --
    #Modifica: tablero
    #Retorna: --
	@abstractmethod
	def crearTablero(self):
        # Metodo que genera
		pass

