from I_Ayuda import I_Ayuda
from interface import implements, Interface
class Ayuda(implements(I_Ayuda)):
    
    def __init__(self):
        pass

    def mostrarReglas(self):
        print ("//Reglas del juego")
        f=open(r"manual.txt") #poner directorio
        manual=f.read()
        return manual
        




