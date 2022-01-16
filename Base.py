from CasillaEspecial import CasillaEspecial

class Base(CasillaEspecial):

    color = ""
    tipo = "base"
    
    #Funcion:Constructor de la base.
    #Requiere: --
    #Modifica: --
    #Retorna: --
    def __init__(self, colorNuevo, posicionParam):
        self.color = colorNuevo
        self.posicion = posicionParam
        self.coordenadaX = 0
        self.coordenadaY = 1

