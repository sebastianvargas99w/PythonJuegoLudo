from I_Ficha import I_Ficha
from interface import implements, Interface
class Ficha(implements(I_Ficha)):
    color =""
    posicion=[]
    base =[]
  
    #Funcion: Constructor para las fichas
    #Requiere: posicion, color, base
    #Modifica: Ficha
    #Retorna: Ficha inicializada
    def __init__(self, posicion,color,base, baseNodo,boton=None,botonVista=None,etiquetaNodo=None):
        self.posicion = posicion
        self.color = color
        self.base = base
        self.baseNodo = baseNodo
        self.boton=boton
        self.botonVista = botonVista
        self.etiquetaNodo = etiquetaNodo

    #Funcion: Pone el color de la ficha
    #Requiere: Inicializar la ficha
    #Modifica: El color
    #Retorna: -
    def setColor(self,color):
        self.color=color

    #Funcion: Asigna la posicion de la ficha en el tablero
    #Requiere: Inicializar la ficha
    #Modifica: La posicion
    #Retorna: -
    def setPos(self,pos):
        self.posicion=pos
    
    #Funcion: Devuelve la posicion de la ficha en el tablero
    #Requiere: Ficha inicializada y posicion valida
    #Modifica: -
    #Retorna: Posicion de la ficha
    def getPos(self):
        return self.posicion
    
    #Funcion: Obtiene el color de la ficha
    #Requiere: Ficha inicializada
    #Modifica: - 
    #Retorna: El color
    def getColor(self):
        return self.color

 