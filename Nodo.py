from Casilla import Casilla

class Nodo:
    etiqueta: Casilla #contenido del nodo en esta solucion sera una casilla
    aristas = []

     #Funcion: Constructor del nodo
    #Requiere: --
    #Modifica: Nodo
    #Retorna: --
    def __init__(self,etiquetaParam):
        self.etiqueta = etiquetaParam
        self.aristas = list()
        
    #Funcion: Agrega una arista a la lista de aristas del nodo.
    #Requiere: Arista, indice
    #Modifica: lista de aristas del nodo
    #Retorna: --
    def asignarArista(self,arista, index):
        # self.aristas.append(arista)
        self.aristas.insert(index, arista)

    #Funcion: Devuelve la posicion de la casilla.
    #Requiere: Requiere que el nodo sea de tipo Casilla
    #Modifica: --
    #Retorna: posicion de la casilla
    def obtenerPosicion(self):
        return self.etiqueta.obtenerPosicion()

    #Funcion: Devuelve las aristas que estan relacionadas con el nodo.
    #Requiere: nodo inicializado
    #Modifica: --
    #Retorna: lista de aristas
    def obtenerAristas(self):
        return self.aristas

    #Funcion: Devuelve la etiqueta del nodo.
    #Requiere: nodo inicializado
    #Modifica: --
    #Retorna: etiqueta
    def obtenerEtiqueta(self):
        return self.etiqueta

    #Funcion: Devuelve una lista con las posiciones de los nodos que estan en la lista de aristas.
    #Requiere: nodo inicializado
    #Modifica: --
    #Retorna: lista de posiciones
    def obtenerPosicionesRelacionadas(self):
        retorno=[]
        for x in self.aristas:
            retorno.append( x.obtenerPrimero().obtenerPosicion() )
            retorno.append(  x.obtenerSegundo().obtenerPosicion() )
        return retorno

    #Funcion: Modifica la etiqueta, se usa para cambiar el tipo de casilla despues de que se creo el tablero.
    #Requiere: nodo inicializado
    #Modifica: etiqueta
    #Retorna: --
    def modificarEtiqueta(self, nuevaEtiqueta):
        self.etiqueta = nuevaEtiqueta
