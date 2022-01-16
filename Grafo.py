from Nodo import Nodo 
from Arista import Arista 

class Grafo:
    nodos = {}#lista de nodos del grafo

    #Constructor de Grafo.
    def __init__(self):
        pass

    #Funcion: Agrega un nodo nuevo al grafo
    #Requiere: nodo nuevo
    #Modifica: grafo
    #Retorna: --
    def agregarNodo(self,nuevoNodo):
        self.nodos[nuevoNodo.obtenerPosicion()] = nuevoNodo

    #Funcion: Devuelve el nodo con la posicion asociada
    #Requiere: posicion
    #Modifica: --
    #Retorna: el nodo con la llave posicion
    
    def obtenerNodo(self,posicion):
        return self.nodos[posicion]

    #Funcion: Agrega una arista al grafo almacenandola en los nodos
    #Requiere: nodo1 y nodo2
    #Modifica: Grafo, nodos
    #Retorna: --
    def agregarArista(self,nodo1,nodo2):
        nuevaArista = Arista( nodo1, nodo2)
        self.nodos[nodo1.obtenerPosicion()].asignarArista(nuevaArista, 1)
        self.nodos[nodo2.obtenerPosicion()].asignarArista(nuevaArista, 0)

    #Funcion: imprime el grafo, este metodo es solamente para pruebas y por eso imprime en consola
    #Requiere: --
    #Modifica: --
    #Retorna: --   
    def imprimir(self):
        dim = 15
        matrix =[]
        for contador in range(0,dim):
            y = [0] * dim
            matrix.append(y)

        print("nodo")
        for key in self.nodos:
            print( self.nodos[key].obtenerPosicion(), end = "")
            print(self.nodos[key].obtenerPosicionesRelacionadas())
            print(str(self.nodos[key].obtenerEtiqueta().coordenadaX) + "," + str(self.nodos[key].obtenerEtiqueta().coordenadaY))


        for x in range(0,dim):
            for y in range(0,dim):
                for key in self.nodos:
                    if key[0] == y and key[1] == x :
                        if self.nodos[key].obtenerEtiqueta().obtenerEspecial()==False:
                            matrix[x][y]=1
                        else:
                            if self.nodos[key].obtenerEtiqueta().obtenerColor() == "verde":
                                matrix[x][y]="G"
                            if self.nodos[key].obtenerEtiqueta().obtenerColor() == "azul":
                                matrix[x][y]="B"
                            if self.nodos[key].obtenerEtiqueta().obtenerColor() == "amarillo":
                                matrix[x][y]="Y"
                            if self.nodos[key].obtenerEtiqueta().obtenerColor() == "rojo":
                                matrix[x][y]="R"
                            if self.nodos[key].obtenerEtiqueta().obtenerColor() == "neutral":
                                matrix[x][y]="*"

        for x in matrix:
            for y in x:
                print(" "+str(y)+" ", end = "")
            print("")