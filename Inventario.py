from I_Inventario import I_Inventario
from interface import implements, Interface
class Inventario(implements(I_Inventario)):
    elementos = []
    def __init__(self):
        self.elementos = []

    def agregar(self,elementoNuevo):
        self.elementos.append(elementoNuevo)

    def quitar(self,elementoEliminar):
        self.elementos.remove(elementoEliminar)

    def esta(self,elemento):
        try:
            indice = self.elementos(elemento)
            return indice
        except:
            return -1;