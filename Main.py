from ModeloTablero import ModeloTablero
from Ayuda import Ayuda
from Jugador import Jugador
from Grafico import Grafico
from Ficha import Ficha
from Controlador import Controlador
import os
from Inventario import Inventario

if __name__ == "__main__":
    ayuda=Ayuda() 
    grafico = Grafico(ayuda)
    controlador=Controlador()
    grafico.ventanaMenu(controlador.obtenerJugadores(),controlador) #aqui ya esta la ventana que llenaa el vector de colores desde la parte gráfica

       
            






       
    
    
