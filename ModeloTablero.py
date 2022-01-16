from Grafo import Grafo
from Nodo import Nodo
from Arista import Arista
from Casilla import Casilla
from IngresarCentro import IngresarCentro
from Centro import Centro
from Base import Base
import itertools
from I_ModeloTablero import I_ModeloTablero
from interface import implements, Interface

class ModeloTablero(implements(I_ModeloTablero)):

    tablero:Grafo
   
    #Constructor de ModeloTablero.
    def __init__(self):
        pass

    #Funcion: Crea un tablero de nodo utilizando un grafo.
    #Requiere: un grafo
    #Modifica: tablero
    #Retorna: tablero creado
    def crearTablero(self):
        dimensionesLudo = 15
        list_coord = [4,208],[36,208],[69,208],[103,208],[136,208],[169,208],[0,0],[238,208],[0,0],[304,208],[337,208],[370,208],[404,208],[437,208],[470,208],[4,240],[36,240],[69,240],[103,240],[136,240],[169,240],[206,240],[0,0],[270,240],[304,240],[337,240],[370,240],[403,240],[437,240],[470,240],[4,272],[36,272],[69,272],[103,272],[136,272],[169,272],[0,0],[238,272],[0,0],[304,272],[337,272],[370,272],[404,272],[437,272],[470,272],[206,5],[206,39],[206,72],[206,105],[206,138],[206,171],[238,5],[238,39],[238,72],[238,105],[238,138],[238,171],[270,5],[270,39],[270,72],[270,105],[270,138],[270,171],[206,303],[206,337],[206,370],[206,403],[206,436],[206,470],[238,303],[238,337],[238,370],[257,423],[238,436],[238,470],[270,303],[270,337],[270,370],[270,403],[270,436],[270,470]
        indice_coord = 0
        self.tablero = Grafo()
        for x in range (6,9):
            for y in range (0,dimensionesLudo):
                self.tablero.agregarNodo((Nodo(Casilla((x,y), list_coord[indice_coord][0],list_coord[indice_coord][1]))))
                indice_coord = indice_coord + 1

        for y in range (6,9):
            for x in range (0,6):
                self.tablero.agregarNodo((Nodo(Casilla((x,y), list_coord[indice_coord][0],list_coord[indice_coord][1]))))
                indice_coord = indice_coord + 1
        for y in range (6,9): 
            for x in range (9,dimensionesLudo):
                self.tablero.agregarNodo((Nodo(Casilla((x,y), list_coord[indice_coord][0],list_coord[indice_coord][1]))))
                indice_coord = indice_coord + 1


        #modifica o agrega casilla para terner las casillas especiales#########################

        self.tablero.obtenerNodo( (7,0) ).modificarEtiqueta( IngresarCentro("Rojo",(7,0), self.tablero.obtenerNodo( (7,0) ).obtenerEtiqueta().coordenadaX, self.tablero.obtenerNodo( (7,0) ).obtenerEtiqueta().coordenadaY))
        self.tablero.obtenerNodo( (0,7) ).modificarEtiqueta( IngresarCentro("Verde",(0,7), self.tablero.obtenerNodo( (0,7) ).obtenerEtiqueta().coordenadaX, self.tablero.obtenerNodo( (0,7) ).obtenerEtiqueta().coordenadaY) )
        self.tablero.obtenerNodo( (14,7) ).modificarEtiqueta( IngresarCentro("Azul",(14,7), self.tablero.obtenerNodo( (14,7) ).obtenerEtiqueta().coordenadaX, self.tablero.obtenerNodo( (14,7) ).obtenerEtiqueta().coordenadaY) )
        self.tablero.obtenerNodo( (7,14) ).modificarEtiqueta( IngresarCentro("Amarillo",(7,14), self.tablero.obtenerNodo((7,14) ).obtenerEtiqueta().coordenadaX, self.tablero.obtenerNodo( (7,14) ).obtenerEtiqueta().coordenadaY) )
        self.tablero.obtenerNodo( (7,7) ).modificarEtiqueta( Centro( (7,7), self.tablero.obtenerNodo( (7,7) ).obtenerEtiqueta().coordenadaX, self.tablero.obtenerNodo( (7,7) ).obtenerEtiqueta().coordenadaY) )
        self.tablero.obtenerNodo( (8,7) ).modificarEtiqueta( Centro( (8,7), self.tablero.obtenerNodo( (8,7) ).obtenerEtiqueta().coordenadaX, self.tablero.obtenerNodo( (8,7) ).obtenerEtiqueta().coordenadaY) )
        self.tablero.obtenerNodo( (6,7) ).modificarEtiqueta( Centro( (6,7), self.tablero.obtenerNodo( (6,7) ).obtenerEtiqueta().coordenadaX, self.tablero.obtenerNodo(  (6,7) ).obtenerEtiqueta().coordenadaY) )
        self.tablero.obtenerNodo( (7,6) ).modificarEtiqueta( Centro( (7,6), self.tablero.obtenerNodo( (7,6) ).obtenerEtiqueta().coordenadaX, self.tablero.obtenerNodo( (7,6) ).obtenerEtiqueta().coordenadaY) )
        self.tablero.obtenerNodo( (7,8) ).modificarEtiqueta( Centro( (7,8), self.tablero.obtenerNodo( (7,8) ).obtenerEtiqueta().coordenadaX, self.tablero.obtenerNodo( (7,8) ).obtenerEtiqueta().coordenadaY) )

        #linea verde

        for contador in range (1,6):
            self.tablero.obtenerNodo( (contador,7) ).modificarEtiqueta( IngresarCentro("Verde",(contador,7), self.tablero.obtenerNodo( (contador,7) ).obtenerEtiqueta().coordenadaX, self.tablero.obtenerNodo(  (contador,7)  ).obtenerEtiqueta().coordenadaY) )

        #linea roja
        for contador in range (1,6):
            self.tablero.obtenerNodo( (7,contador) ).modificarEtiqueta( IngresarCentro("Rojo",(7,contador), self.tablero.obtenerNodo( (7,contador) ).obtenerEtiqueta().coordenadaX, self.tablero.obtenerNodo( (7,contador) ).obtenerEtiqueta().coordenadaY) )

        #linea azul
        for contador in range (9,14):
            self.tablero.obtenerNodo( (contador,7) ).modificarEtiqueta( IngresarCentro("Azul",(contador,7), self.tablero.obtenerNodo( (contador,7) ).obtenerEtiqueta().coordenadaX, self.tablero.obtenerNodo( (contador,7) ).obtenerEtiqueta().coordenadaY) )

        #linea amarilla
        for contador in range (9,14):
            self.tablero.obtenerNodo( (7,contador) ).modificarEtiqueta( IngresarCentro("Amarillo",(7,contador), self.tablero.obtenerNodo( (7,contador) ).obtenerEtiqueta().coordenadaX, self.tablero.obtenerNodo( (7,contador)   ).obtenerEtiqueta().coordenadaY) )


        #agregando bases

        self.tablero.agregarNodo((Nodo(   Base(  "Verde",(1,9)    ))))
        self.tablero.agregarNodo((Nodo(   Base(  "Rojo",(5,1)    ))))
        self.tablero.agregarNodo((Nodo(   Base(  "Azul",(13,5)    ))))
        self.tablero.agregarNodo((Nodo(   Base(  "Amarillo",(9,13)    ))))
        #se terminaron de agregar las casillas especiales###################################




        #agregando aristas al tablero
        # fila 6
        for x in range( 0, 5):
            self.tablero.agregarArista(self.tablero.obtenerNodo((6,x)),self.tablero.obtenerNodo((6,x+1)))
        for x in range( 9, 14):
            self.tablero.agregarArista(self.tablero.obtenerNodo((6,x)),self.tablero.obtenerNodo((6,x+1)))
        # Fila 6 Caso Esquina
        self.tablero.agregarArista(self.tablero.obtenerNodo((6,5)),self.tablero.obtenerNodo((5,6)))
        self.tablero.agregarArista(self.tablero.obtenerNodo((6,14)),self.tablero.obtenerNodo((7,14)))

        # fila 7
        for x in range( 1, 6):
            self.tablero.agregarArista(self.tablero.obtenerNodo((7,x)),self.tablero.obtenerNodo((7,x+1)))
        for x in range( 8, 13):
            self.tablero.agregarArista(self.tablero.obtenerNodo((7,x+1)),self.tablero.obtenerNodo((7,x)))

        # Fila 7 Caso especial
        self.tablero.agregarArista(self.tablero.obtenerNodo((7,0)),self.tablero.obtenerNodo((6,0)))
        self.tablero.agregarArista(self.tablero.obtenerNodo((7,14)),self.tablero.obtenerNodo((8,14)))
        #columna 7 ingresar centro
        nuevaArista0 = Arista( self.tablero.obtenerNodo((7,0)), self.tablero.obtenerNodo((7,1)))
        self.tablero.obtenerNodo((7,0)).asignarArista(nuevaArista0, 3)
        self.tablero.obtenerNodo((7,1)).asignarArista(nuevaArista0, 0)
        nuevaArista3 = Arista( self.tablero.obtenerNodo((7,14)), self.tablero.obtenerNodo((7,13)))
        self.tablero.obtenerNodo((7,14)).asignarArista(nuevaArista3, 3)
        self.tablero.obtenerNodo((7,13)).asignarArista(nuevaArista3, 0)



        # fila 8
        for x in range( 0, 5):
            self.tablero.agregarArista(self.tablero.obtenerNodo((8,x+1)),self.tablero.obtenerNodo((8,x)))
        for x in range( 9, 14):
            self.tablero.agregarArista(self.tablero.obtenerNodo((8,x+1)),self.tablero.obtenerNodo((8,x)))
        # Fila 8 Caso Esquina
        self.tablero.agregarArista(self.tablero.obtenerNodo((8,0)),self.tablero.obtenerNodo((7,0)))
        self.tablero.agregarArista(self.tablero.obtenerNodo((8,9)),self.tablero.obtenerNodo((9,8)))


         # columna 6
        for x in range( 0, 5):
            self.tablero.agregarArista(self.tablero.obtenerNodo((x+1,6)),self.tablero.obtenerNodo((x,6)))
        for x in range( 9, 14):
            self.tablero.agregarArista(self.tablero.obtenerNodo((x+1,6)),self.tablero.obtenerNodo((x,6)))
         # columa 6 Caso Esquina
        self.tablero.agregarArista(self.tablero.obtenerNodo((0,6)),self.tablero.obtenerNodo((0,7)))
        self.tablero.agregarArista(self.tablero.obtenerNodo((9,6)),self.tablero.obtenerNodo((8,5)))

        # columna 7
        for x in range( 1, 6):
            self.tablero.agregarArista(self.tablero.obtenerNodo((x,7)),self.tablero.obtenerNodo((x+1,7)))
        for x in range( 8, 13):
            self.tablero.agregarArista(self.tablero.obtenerNodo((x+1,7)),self.tablero.obtenerNodo((x,7)))

        # columna 7 Caso Esquina
        self.tablero.agregarArista(self.tablero.obtenerNodo((0,7)),self.tablero.obtenerNodo((0,8)))
        self.tablero.agregarArista(self.tablero.obtenerNodo((14,7)),self.tablero.obtenerNodo((14,6)))
        #columna 7 ingresar centro
        nuevaArista1 = Arista( self.tablero.obtenerNodo((0,7)), self.tablero.obtenerNodo((1,7)))
        self.tablero.obtenerNodo((0,7)).asignarArista(nuevaArista1, 3)
        self.tablero.obtenerNodo((1,7)).asignarArista(nuevaArista1, 0)
        nuevaArista2 = Arista( self.tablero.obtenerNodo((14,7)), self.tablero.obtenerNodo((13,7)))
        self.tablero.obtenerNodo((14,7)).asignarArista(nuevaArista2, 3)
        self.tablero.obtenerNodo((13,7)).asignarArista(nuevaArista2, 0)

        # columna 8
        for x in range( 0, 5):
            self.tablero.agregarArista(self.tablero.obtenerNodo((x,8)),self.tablero.obtenerNodo((x+1,8)))
        for x in range( 9, 14):
            self.tablero.agregarArista(self.tablero.obtenerNodo((x,8)),self.tablero.obtenerNodo((x+1,8)))
        # columna 8 Caso Esquina
        self.tablero.agregarArista(self.tablero.obtenerNodo((5,8)),self.tablero.obtenerNodo((6,9)))
        self.tablero.agregarArista(self.tablero.obtenerNodo((14,8)),self.tablero.obtenerNodo((14,7)))


        return

    #Funcion: imprime el tablero, este metodo es solo de pruebas
    #Requiere: tablero inicializado
    #Modifica: -
    #Retorna: -
    def imprimirTablero(self):
        self.tablero.imprimir()
