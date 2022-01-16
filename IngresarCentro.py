from CasillaEspecial import CasillaEspecial

class IngresarCentro(CasillaEspecial):

    color = ""
    tipo = "ingresarCentro"
    numeroCasillas=0
    coordenadaX = 0
    coordenadaY = 0
    
    #Funcion:Constructor de IngresarCentro, estas son las casillas las ultimas casillas para ingresar al centro
    #Requiere: --
    #Modifica: --
    #Retorna: --
    def __init__(self, colorNuevo, posicionParam, coordenadaX, coordenadaY):
        self.color = colorNuevo
        self.posicion = posicionParam
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY        

