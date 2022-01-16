from CasillaEspecial import CasillaEspecial

class Centro(CasillaEspecial):

    color = "neutral"
    tipo = "centro"

    #Constructor para el centro del tablero
    def __init__(self, posicionParam, coordenadaX, coordenadaY):
        self.posicion = posicionParam
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY



