import Ficha
from I_Casilla import I_Casilla
from interface import implements, Interface

class Casilla(implements(I_Casilla)):
    especial:bool
    posicion = None
    fichas = [] #lista de fichas que estan en la casilla
    coordenadaX = 0
    tipo = "Normal"

    #Constructor de Casilla.
    def __init__(self, posicionParam, coordenadaX,coordenadaY):
        self.posicion = posicionParam
        self.especial = False
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
        self.tipo = "Normal"
        self.fichas= []
        
    #Ubica una ficha en la casilla.
    def agregarFicha(self,ficha,controlador):
        if len(self.fichas) == 0 or ficha.etiquetaNodo.obtenerEtiqueta().tipo == "centro":
            self.fichas.append(ficha)
        elif len(self.fichas) >= 1 and self.fichas[0].color != ficha.color:
            controlador.comer(self.fichas[0])
            self.sacarFicha()
            self.fichas.append(ficha)

    #Saca a la ultima ficha que ingreso, otro metodo la movera despues.
    def sacarFicha(self):
        return self.fichas.pop

    #Devuelve las coordenadas de la casilla como si fuera una matriz.
    def obtenerPosicion(self):
        return self.posicion

    #Se usa para para indicar que una casilla tendra un comportamiento especial.
    def cambiarEspecial(self,nuevoValor):
        self.especial = nuevoValor

    #Devuelve un booleano que indica si la casilla es especial.
    def obtenerEspecial(self):
        return self.especial


