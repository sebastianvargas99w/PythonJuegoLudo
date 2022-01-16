from Nodo import Nodo

class Arista:
    primerNodo:Nodo
    segundoNodo:Nodo

    #Funcion: Constructor de la arista
    #Requiere: -
    #Modifica: Arista
    #Retorna: -
    def __init__(self,primero,segundo):
        self.primerNodo = primero
        self.segundoNodo = segundo

    #Funcion: Devuelve el nodo 1 de la arista
    #Requiere: Arista inicializada
    #Modifica: -
    #Retorna: nodo
    def obtenerPrimero(self):
        return self.primerNodo

    #Funcion: Devuelve el nodo 2 de la arista
    #Requiere: Arista inicializada
    #Modifica: -
    #Retorna: nodo
    def obtenerSegundo(self):
        return self.segundoNodo

    #Funcion: Devuelve una tupla con los nodos de la arista
    #Requiere: Arista inicializada
    #Modifica: -
    #Retorna: tupla
    def obtenerNodos(self):
        return self.primerNodo,self.segundoNodo