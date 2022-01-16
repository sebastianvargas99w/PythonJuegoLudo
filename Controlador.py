from ModeloTablero import ModeloTablero
from Ayuda import Ayuda
from Jugador import Jugador
from Ficha import Ficha
from tkinter import Tk, Button, Menu, Label, Canvas, PhotoImage,Pack, NW
from PIL import Image, ImageTk
import random
from tkinter import messagebox
from tkinter import BOTH, END, LEFT
from tkinter import filedialog
from tkinter import Entry
import tkinter as tk
import os
from GestorPartidas import GestorPartidas
import os
from I_Controlador import I_Controlador
from interface import implements, Interface

class Controlador(implements(I_Controlador)):
    #Constructor del controlador
    def __init__(self,dado=None,jugadorEnTurno=None, tablero = None):
        self.jugadores = []
        self.dado=dado
        self.jugadorEnTurno =jugadorEnTurno
        self.tablero = ModeloTablero()
        self.tablero.crearTablero()
        self.jugadoresGanaron = []

    #Funcion: inicializa las bases y las casillas iniciales de los jugadores dependiendo de la cantidad y color de jugadores que el usuario indique
    #Requiere: lista de jugadores
    #Modifica: Jugadores
    #Retorna: Jugadores inicializados
    def iniciarJugadores(self,jugadores): #
        for i in range(0, len(self.jugadores)):
            if jugadores[i].color=="Azul":
                jugadores[i].base =(36,320) #x hasta 150, y hasta 450
                jugadores[i].casillaInicial = self.tablero.tablero.obtenerNodo((13,6))
                
            if jugadores[i].color=="Rojo":
                jugadores[i].base = (10,10)# y hasta 150 x hasta 150
                jugadores[i].casillaInicial = self.tablero.tablero.obtenerNodo((6,1))
                
            if jugadores[i].color=="Amarillo":
                jugadores[i].base = (310,310) # de 310 a 450
                jugadores[i].casillaInicial = self.tablero.tablero.obtenerNodo((8,13))

            if jugadores[i].color=="Verde":
                jugadores[i].base = (310,0) #x de 310 a 450 y de 0 a 150
                jugadores[i].casillaInicial = self.tablero.tablero.obtenerNodo((1,8))
              

    #Funcion: Pone el color de los jugadores que el usuario elija
    #Requiere: jugador, color
    #Modifica: Jugador
    #Retorna: -
    def escogeColor(self,Jugador,color):
        Jugador.setColor(color)

    #Funcion: Mueve fichas en el tablero
    #Requiere: jugador, ficha,tablero
    #Modifica: Posicion de la ficha
    #Retorna: -
    def moverFicha(self,jugador,ficha):
        pass

    #Funcion: Escoge colores en consola para cada jugador
    #Requiere: -
    #Modifica: Jugador y lista de jugadores
    #Retorna: -
    def escogerColores(self):
        for i in range (0,4):
            jugador=Jugador()
            print("\nDatos para Jugador "+str(i))
            color=input("Que color quiere usar?\n")
            self.escogeColor(jugador,color)
            self.jugadores.append(jugador)
        
    #Funcion: Escoge el primer jugador de la partida
    #Requiere: label para informar
    #Modifica: turnos de jugadores
    #Retorna: -
    def escogerPrimero(self,labT):
        orden = 0
        primero =0
        jprimero=0
        tiradas=" "
        for i in range(0, len(self.jugadores)):
            dado = random.randint(1,6)
            tiradas =tiradas + ("\nJugador "+self.jugadores[i].getColor()+" Tiró el dado y salió "+str(dado))
            orden =dado
            if primero < orden:
                primero = orden
                jprimero = i
        self.jugadorEnTurno=jprimero
        self.jugadores[jprimero].setTurno(True)
        print(tiradas)
        labT.configure(text = tiradas )
        return jprimero

    #Funcion: Tira el dado para jugar
    #Requiere: -
    #Modifica: -
    #Retorna: dado
    def tirarDado(self):
        self.dado = random.randint(1,6)
        return self.dado

    #Funcion: Cambia de turno para seguir el orden del juego
    #Requiere: -
    #Modifica: jugador en turno
    #Retorna: -
    def cambiarTurno(self):
        self.jugadores[self.jugadorEnTurno].setTurno(False)
        proxjt = self.jugadorEnTurno + 1
        if (proxjt >= len(self.jugadores)):
            proxjt = 0
        while proxjt in self.jugadoresGanaron:
            proxjt = proxjt +1
            if (proxjt >= len(self.jugadores)):
                proxjt = 0



        if (proxjt < len(self.jugadores)):
            self.jugadorEnTurno = proxjt
            self.jugadores[self.jugadorEnTurno].setTurno(True)

        else:
            self.jugadorEnTurno=0
            self.jugadores[self.jugadorEnTurno].setTurno(True)
        

    #Funcion: Carga una partida guardada
    #Requiere: archivo
    #Modifica: -
    #Retorna: -
    def cargar(self, archivo):
        gestor = GestorPartidas()
        self.tablero,self.jugadores,self.jugadorEnTurno,self.dado = gestor.cargar(archivo)
       
    #Funcion: Guarda la partida actual
    #Requiere: archivo
    #Modifica: archivo
    #Retorna: -
    def guardar(self, archivo):
        gestor = GestorPartidas()
        gestor.guardar(archivo,self.tablero,self.jugadores,self.jugadorEnTurno,self.dado)

    #Funcion: Reinicia la lista de jugadores
    #Requiere: -
    #Modifica: lista de jugadores
    #Retorna: -
    def resetJugadores(self):
        self.jugadores[:] = []

    #Funcion: Obtiene lista de jugadores
    #Requiere: -
    #Modifica: -
    #Retorna: lista de jugadores
    def obtenerJugadores(self):
        return self.jugadores

    #Funcion: Regresa una ficha a su base 
    #Requiere: Ficha inicializada 
    #Modifica: Posicion de la ficha
    #Retorna: -
    def comer(self,ficha):
        ficha.posicion = ficha.base
        ficha.etiquetaNodo = ficha.baseNodo
    
    #Funcion: Determina si un jugador gano la partida cuando sus 4 fichas estan en el centro
    #Requiere: Jugadores inicializados, 4 fichas en el centro de cualquier jugador
    #Modifica: Lista de jugadores, lista de jugadores ganadores
    #Retorna: -
    def terminado(self,par1 = None,par2 = None,j = None):
        ter=0
        lab = par1
        jugadores = par2
        for i in range(0,4):
            if(jugadores[j].fichas[i].etiquetaNodo.obtenerEtiqueta().tipo == "centro"):
                ter+=1
        if(ter == 4):
            lab.configure(text ="Ganó el jugador" + jugadores[j].getColor())
            self.jugadoresGanaron.append(j)
           

    
        



        
