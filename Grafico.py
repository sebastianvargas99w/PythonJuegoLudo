from ModeloTablero import ModeloTablero
from I_Ayuda import I_Ayuda
from Jugador import Jugador
from Ficha import Ficha
from Controlador import Controlador
from tkinter import Tk, Button, Menu, Label, Canvas, PhotoImage,Pack, NW,FLAT,Frame,DISABLED,NORMAL
from PIL import Image, ImageTk
import random
from tkinter import messagebox
from tkinter import BOTH, END, LEFT
from tkinter import filedialog
from tkinter import Entry
from I_Grafico import I_Grafico
import tkinter as tk
import os
from GestorPartidas import GestorPartidas
import os
from interface import implements, Interface
class Grafico(implements(I_Grafico)):
    control=Controlador
    fichas =[] #fichas en el canvas

    #Funcion: Constructor de la clase 
    #Requiere: -- 
    #Modifica: Define las variables globales 
    #Retorna: --
    def __init__(self,ayuda,cantJug=0,etyColores=None,MenPlColores=None,labEsCol=None,labPrimero=None,labEtPri=None,btnAcNum=None,btnAcColor=None,empezar=None):
        self.cantJug=cantJug
        self.ayuda=ayuda
        self.control=Controlador()
        self.reinicio=False
        self.etyColores=etyColores
        self.MenPlColores=MenPlColores
        self.labEsCol=labEsCol
        self.labPrimero=labPrimero
        self.labEtPri=labEtPri
        self.btnAcNum=btnAcNum
        self.btnAcColor=btnAcColor
        self.empezar=empezar
    def resetMenu(self,jugadores,controlador):
        self.btnAcNum.place_forget()
        self.btnAcColor['state'] = tk.NORMAL
        self.btnAcNum['state'] = tk.NORMAL
        #entry2.place_forget()
        controlador.resetJugadores()
        self.labEsCol.configure(text = " " )
        self.labPrimero.configure(text = " " )
        self.labEtPri.configure(text = " " )
        self.MenPlColores['menu'].entryconfigure(0, state=tk.NORMAL)
        self.MenPlColores['menu'].entryconfigure(1, state=tk.NORMAL)
        self.MenPlColores['menu'].entryconfigure(2, state=tk.NORMAL)
        self.MenPlColores['menu'].entryconfigure(3, state=tk.NORMAL)

    def cargarTablero(self,ventanaMenu,controlador,jugadores,cargando = 0):
        ventanaMenu.state(newstate = "withdraw")
        self.ventana(controlador.obtenerJugadores(),controlador,ventanaMenu,cargando)
        
        #Funcion: Define los colores de cada jugador
        #Requiere: La entrada del color obtenido en la venta del menu y la lista de jugadores no vacia
        #Modifica: Los colores de cada jugador
        #Retorna: --
    def defineCol(self,valor,jugadores,controlador,OPTColores):
        jugador=Jugador()
        controlador.escogeColor(jugador,valor)
        jugadores.append(jugador)
        self.cantJug=int(self.cantJug-1)
        if self.cantJug>0 :
            self.labEsCol.configure(text = "Ingrese el color del jugador "+ str (self.cantJug) )
            self.cantJug=int(self.cantJug)
            self.MenPlColores['menu'].entryconfigure(valor, state=tk.DISABLED) 
        else :
            primero =controlador.escogerPrimero(self.labPrimero)
            self.labEtPri.configure(text = "El primero en jugar es el "+ jugadores[primero].getColor() )
            self.labPrimero.place(x=200, y=210)
            self.labEtPri.place(x=200, y=200)
            self.btnAcNum['state'] = tk.DISABLED
            self.empezar.place(x=400, y=200)
        #entry2.delete(0, END)

        #Funcion: Procesa los datos ingresados y define la cantidad de jugadores
        #Requiere: El valor con la cantidad de jugadores obtenido de la ventana de menu principal
        #Modifica: La variable con la cantidad de jugadores
        #Retorna: --
    def proc(self,valor):
       self.cantJug=int(valor)
       self.MenPlColores.place(x=250, y=130)
       self.labEsCol.configure(text = "Ingrese el color del jugador "+valor )
       self.btnAcNum.place(x=250, y=170)
       self.btnAcColor['state'] = tk.DISABLED
    
    def manual(self):
        manual=self.ayuda.mostrarReglas()
        messagebox.showinfo("Manual",manual)

    def notificar(self,texto):
        messagebox.showinfo("Ludo",texto)


    def resetVenJu(self,windows,ventanaMenu,jugadores,controlador):
       #lab.configure(text='Inicio')
        ventanaMenu.state(newstate = "normal")
        self.resetMenu(jugadores,controlador)
        ventanaMenu.call('wm', 'attributes', '.', '-topmost', '1')
        windows.destroy()
       
    def cargar(self,window,controlador,jugadores):
        window.filename =  filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("Binary","*.ludo"),("all files","*.*")),defaultextension = ".ludo",multiple = False)
        if window.filename =='':
            self.notificar("No se cargo ningun archivo")
        else:
            print(window.filename)
            controlador.cargar(window.filename)
            self.cargarTablero(window,controlador,jugadores,1)
            self.notificar("Archivo cargado desde "+ window.filename)
            #self.actualizar(self.canvas, controlador.jugadores)

        
    def guardar(self,window,controlador):
        window.filename =  filedialog.asksaveasfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("Binary","*.ludo"),("all files","*.*")),defaultextension = ".ludo")
        if window.filename =='':
            self.notificar("No se guardo ningun archivo")
        else:
            print (window.filename)
            controlador.guardar(window.filename)
            self.notificar("Archivo guardado en " + window.filename)

        #Funcion: Es la representación grafica de tirar los dados
        #Requiere: La etiquetas doode se muestra el valor de los dados
        #Modifica: La  etiqueta
        #Retorna: --
    def clicked(self,label, label6,controlador,jugadores):
        dado = controlador.tirarDado()
        label.configure(text = str(dado) )


    def cambiarTurnos(self,label,controlador,jugadores):
        controlador.cambiarTurno()
        label.configure(text=jugadores[controlador.jugadorEnTurno].getColor())
   

    def ventanaMenu(self, jugadores,controlador):
        venMenu=Tk()
        venMenu.title("Ludo")
        venMenu.geometry('700x500+300+150')
        venMenu.resizable(width=True,height=True)
        menu =Menu(venMenu)
        new=Menu(menu)
        labNumJug =Label(venMenu,text="Cuantos jugadores van a jugar")
        #lab6 = Label(venMenu, text = " ")
        #lab6.grid(column = 10, row = 2)
        labNumJug.place(x=200, y=30)
          #entradas de texto
        OPTNumJug = [ #Opciones de cantidad de jugadores
        "2",
        "3",
        "4"
        ] 
        etyNumJug = tk.StringVar(venMenu) #Entrada numero de jugadores
        etyNumJug.set(OPTNumJug[0])
        MenPlNumJug = tk.OptionMenu(venMenu, etyNumJug, *OPTNumJug)
        MenPlNumJug.place(x=250, y=50)
        #entryMenu = Entry(venMenu)
        self.etyColores = Entry(venMenu)
        OPTColores = [
        "Rojo",
        "Amarillo",
        "Azul",
        "Verde"
        ]
        self.etyColores = tk.StringVar(venMenu)
        self.MenPlColores = tk.OptionMenu(venMenu, self.etyColores, *OPTColores)
        self.labEsCol =Label(venMenu,text=" ") # self.labEsCol = labCor
        self.labEsCol.place(x=200, y=120)
        self.labPrimero =Label(venMenu,text=" ") #self.labPrimero = labT
        self.labEtPri = Label(venMenu,text=" ")  #self.labEtPri = labP                  self.btnAcNum = ac
        self.btnAcNum = Button(venMenu, text= "Aceptar", command=lambda:self.defineCol(self.etyColores.get(),jugadores,controlador,OPTColores))
        #self.btnAcColor = acpt
        self.btnAcColor = Button(venMenu, text= "Aceptar", command=lambda:self.proc(etyNumJug.get()))
        self.btnAcColor.place(x=250, y=90)                                              
        self.empezar = Button(venMenu, text= "Empezar juego", command=lambda:self.cargarTablero(venMenu,controlador,jugadores,0))
        controlador.iniciarJugadores(jugadores)
        #Pestanas
        new.add_command(label='Manual',command=self.manual)
        new.add_separator()
        new.add_command(label="Nueva Partida",command=lambda: self.resetMenu(jugadores,controlador))
        new.add_separator()
        new.add_command(label="Cargar Partida",command=lambda:self.cargar(venMenu,controlador,jugadores))

        menu.add_cascade(label = 'Opciones',menu=new)
        venMenu.config(menu=menu)
        venMenu.mainloop()

        #Funcion: Actualiza la posicion de las fichas en el tablero en la ventana del juego
        #Requiere: El canvas donde se colocan las fichas
        #Modifica: La posición grafica de las fichas
        #Retorna: -- 
    def actualizar(self,canvas,jugadores):
        for i in range(0, len(jugadores)):
            for f in range(0,4):
                canvas.coords(jugadores[i].fichas[f].botonVista,jugadores[i].fichas[f].posicion)

        #Funcion: Mueve las fichas en la estructura logica
        #Requiere: La estructura con las fichas y los jugadores
        #Modifica: La posicion de las fichas en la estructua
        #Retorna: -- 
    def moverFicha(self,button,canvas,jugadores,i,j,controlador,lab,lab2,lab3):
        if (jugadores[controlador.jugadorEnTurno].getColor() == jugadores[i].fichas[j].getColor()):
            self.actualizar(canvas,jugadores)
            dado= int(lab)

            etiq = jugadores[i].fichas[j].etiquetaNodo
            tipo = etiq.obtenerEtiqueta().tipo
            print (tipo)
            if (dado == 6 and tipo == "base" ):
                etiq= jugadores[i].casillaInicial
                jugadores[i].fichas[j].posicion[0] = etiq.obtenerEtiqueta().coordenadaX
                jugadores[i].fichas[j].posicion[1] = etiq.obtenerEtiqueta().coordenadaY
                jugadores[i].fichas[j].etiquetaNodo = etiq
                canvas.coords(jugadores[i].fichas[j].botonVista,jugadores[i].fichas[j].posicion)

            elif (tipo == "Normal"):
                jugadores[i].fichas[j].etiquetaNodo.obtenerEtiqueta().sacarFicha()
                for f in range (0, dado):
                    temp = etiq.obtenerAristas()[1].obtenerSegundo()
                    etiq = temp
                    if(etiq.obtenerEtiqueta().tipo == "ingresarCentro" and (etiq.obtenerEtiqueta().posicion == (7,0) or etiq.obtenerEtiqueta().posicion == (7,14) or etiq.obtenerEtiqueta().posicion == (0,7) or etiq.obtenerEtiqueta().posicion == (14,7)  )):
                        if(etiq.obtenerEtiqueta().color == jugadores[i].fichas[j].getColor()):
                            temp = etiq.obtenerAristas()[2].obtenerSegundo()
                            etiq = temp 
                            f = f + 1                       
                # print (jugadores[i].fichas[j].posicion)
                jugadores[i].fichas[j].posicion[0] = etiq.obtenerEtiqueta().coordenadaX
                jugadores[i].fichas[j].posicion[1] = etiq.obtenerEtiqueta().coordenadaY
                jugadores[i].fichas[j].etiquetaNodo = etiq
                # print (jugadores[i].fichas[j].posicion)
                canvas.coords(jugadores[i].fichas[j].botonVista,jugadores[i].fichas[j].posicion)
                pos = jugadores[i].fichas[j].etiquetaNodo.obtenerPosicion()
                controlador.tablero.tablero.obtenerNodo(pos).obtenerEtiqueta().agregarFicha(jugadores[i].fichas[j], controlador)
            elif (tipo == "ingresarCentro"):
                if(etiq.obtenerEtiqueta().color == jugadores[i].getColor()):

                    espacios=0
                    if (etiq.obtenerEtiqueta().posicion == (7,0) or etiq.obtenerEtiqueta().posicion == (7,14) or etiq.obtenerEtiqueta().posicion == (0,7) or etiq.obtenerEtiqueta().posicion == (14,7)  ):
                        temp = etiq.obtenerAristas()[2].obtenerSegundo()
                        tipo = temp.obtenerEtiqueta().tipo
                        etiq = temp
                        espacios = 1
                    
                    while(tipo !="centro"):
                        temp = etiq.obtenerAristas()[1].obtenerSegundo()
                        tipo = temp.obtenerEtiqueta().tipo
                        etiq = temp
                        espacios+=1
                    if(dado <= espacios):
                        et = jugadores[i].fichas[j].etiquetaNodo
                        for f in range (0, dado):
                            sig = et.obtenerAristas()[1].obtenerSegundo()
                            et = sig
                        jugadores[i].fichas[j].posicion[0] = et.obtenerEtiqueta().coordenadaX
                        jugadores[i].fichas[j].posicion[1] = et.obtenerEtiqueta().coordenadaY
                        jugadores[i].fichas[j].etiquetaNodo = et
                        canvas.coords(jugadores[i].fichas[j].botonVista,jugadores[i].fichas[j].posicion)
                        if(dado == espacios):
                            controlador.terminado(lab3,jugadores,i)

                else:   
                    for f in range (0, dado):
                        temp = etiq.obtenerAristas()[1].obtenerSegundo()
                        etiq = temp
                                        
                    # print (jugadores[i].fichas[j].posicion)
                    jugadores[i].fichas[j].posicion[0] = etiq.obtenerEtiqueta().coordenadaX
                    jugadores[i].fichas[j].posicion[1] = etiq.obtenerEtiqueta().coordenadaY
                    jugadores[i].fichas[j].etiquetaNodo = etiq
                    # print (jugadores[i].fichas[j].posicion)
                    canvas.coords(jugadores[i].fichas[j].botonVista,jugadores[i].fichas[j].posicion)
                    jugadores[i].fichas[j].etiquetaNodo.obtenerEtiqueta().agregarFicha(jugadores[i].fichas[j], controlador)

            if (dado != 6):
                self.cambiarTurnos(lab2,controlador,jugadores)   
            self.actualizar(canvas,jugadores)    
                
            
        
       

    def ventana(self, jugadores,controlador,venMenu,cargando =0):
        controlador.iniciarJugadores(jugadores) #inicializa los jugadores 
        #ventana de juego
        window=tk.Toplevel(venMenu)
        window.title("Ludo")
        window.geometry('700x500+300+150')
        window.resizable(width=True,height=True)

        #canvas
        canvas = tk.Canvas(window, width=500,height=500)
        canvas.pack(side="left", fill="both", expand=True) 
        #tablero
        image = Image.open("Ludo_Board.png")
        image = image.resize((500, 500), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        tabl=ImageTk.PhotoImage(image)
        background = canvas.create_image(1,1,anchor=NW,image=tabl)
        
        buttonFrame = Frame(window) #frame para los botones y labels
        buttonFrame.pack( fill="both", expand=False)
        

        
        labAviso=Label(buttonFrame, text = " ") 
        labAviso.grid(row=0, column=0)
        orden=Label(buttonFrame, text = "                   ") 
        orden.grid(row=0, column=1)
        lab = None
        if controlador.dado != 0:
            lab =Label(buttonFrame, text= str(controlador.dado) ) #muestra dado
        else:
            lab =Label(buttonFrame,text="Inicio") #muestra dado

        dado = Button(buttonFrame, text= "Dado", command=lambda:self.clicked(lab, labAviso,controlador,jugadores))

        lab.grid(row=2, column=0)
        dado.grid(row=3, column=0)
        botonPT = Button(buttonFrame, text= "Pasar Turno", command=lambda:self.cambiarTurnos(usuario,controlador,jugadores))
        botonPT.grid(row=5, column=0)
        usuario = Label(buttonFrame,text=jugadores[controlador.jugadorEnTurno].getColor())
        usuario.grid(row=4, column=0)
        ganadores = Label(buttonFrame,text="Ganadores")
        ganadores.grid(row=6, column=0)
        
        if cargando ==1:
            contador = 0
            for contador in range (0, len(controlador.jugadores)):
                for itFicha in range (0,4):
                    button = Button(window, text = "" )
                    if(controlador.jugadores[contador].color=="Azul"): 
                        button.configure(width = 2, activebackground = "#2081C3",background="#2081C3")
                        x = controlador.jugadores[contador].fichas[itFicha].posicion[0]
                        y = controlador.jugadores[contador].fichas[itFicha].posicion[1]
                        button_window = canvas.create_window(x,y, anchor=NW, window=button)
                        controlador.jugadores[contador].fichas[itFicha].boton = button
                        controlador.jugadores[contador].fichas[itFicha].botonVista = button_window
                    elif(controlador.jugadores[contador].color=="Rojo"):
                        button.configure(width = 2, activebackground = "#FF1654",background="#FF1654")
                        x = controlador.jugadores[contador].fichas[itFicha].posicion[0]
                        y = controlador.jugadores[contador].fichas[itFicha].posicion[1]
                        button_window = canvas.create_window(x,y, anchor=NW, window=button)
                        controlador.jugadores[contador].fichas[itFicha].boton = button
                        controlador.jugadores[contador].fichas[itFicha].botonVista = button_window
                        
                    elif(controlador.jugadores[contador].color=="Amarillo"):
                        button.configure(width = 2, activebackground = "#FDC90D",background="#FDC90D")
                        x = controlador.jugadores[contador].fichas[itFicha].posicion[0]
                        y = controlador.jugadores[contador].fichas[itFicha].posicion[1]
                        button_window = canvas.create_window(x,y, anchor=NW, window=button)
                        controlador.jugadores[contador].fichas[itFicha].boton = button
                        controlador.jugadores[contador].fichas[itFicha].botonVista = button_window
                    elif(controlador.jugadores[contador].color=="Verde"):
                        button.configure(width = 2, activebackground = "#2E933C",background="#2E933C")
                        x = controlador.jugadores[contador].fichas[itFicha].posicion[0]
                        y = controlador.jugadores[contador].fichas[itFicha].posicion[1]
                        button_window = canvas.create_window(x,y, anchor=NW, window=button)
                        controlador.jugadores[contador].fichas[itFicha].boton = button
                        controlador.jugadores[contador].fichas[itFicha].botonVista = button_window
                
                
        else:
            self.crearFichas(window,canvas,jugadores,controlador,lab) #pone las fichas
        self.configurarBotones(jugadores,canvas,controlador,lab,usuario,ganadores)


        menu =Menu(window)
        new=Menu(menu)
        new.add_command(label='Manual',command=self.manual)
        new.add_separator()
        new.add_command(label="Nueva Partida",command=lambda: self.resetVenJu(window,venMenu,jugadores,controlador))
        new.add_separator()
        new.add_command(label="Cargar Partida",command=lambda:self.cargar(window,controlador,jugadores))
        new.add_separator()
        new.add_command(label="Guardar Partida",command=lambda:self.guardar(window,controlador))
        menu.add_cascade(label = 'Opciones',menu=new)
        
        window.config(menu=menu)
        window.mainloop()
     
       
        #Funcion: Coloca las fichas en la ventana grafica la primera vez al iniciar la partida
        #Requiere: Un canvas para colocar las fichas al iniciar la partida
        #Modifica: El canvas de la ventana de juego
        #Retorna: ---
    def crearFichas(self,window,canvas,jugadores,controlador,lab):
        for i in range(0, len(jugadores)):
            
            if(jugadores[i].color=="Azul"): 
                x=jugadores[i].base[0]
                y=jugadores[i].base[1]
                for j in range(0,4):
                    x +=15
                    y +=10
                    button1 = Button(window, text = "" )
                    button1.configure(width = 2, activebackground = "#2081C3",background="#2081C3")
                    button1_window = canvas.create_window(x,y, anchor=NW, window=button1)
                    ficha = Ficha([x,y],"Azul",[x,y],self.control.tablero.tablero.obtenerNodo((13,5)),button1,button1_window,self.control.tablero.tablero.obtenerNodo((13,5)))
                    jugadores[i].fichas.append(ficha) 

            elif(jugadores[i].color=="Rojo"):
                x=jugadores[i].base[0]
                y=jugadores[i].base[1]
                for j in range(0,4):
                    x+=15
                    y+=10
                    button2 = Button(window, text = "" )
                    button2.configure(width = 2, activebackground = "#FF1654",background="#FF1654")
                    button2_window = canvas.create_window(x,y, anchor=NW, window=button2)
                    ficha = Ficha([x,y],"Rojo",[x,y],self.control.tablero.tablero.obtenerNodo((5,1)),button2,button2_window,self.control.tablero.tablero.obtenerNodo((5,1)))
                    jugadores[i].fichas.append(ficha) 

            elif(jugadores[i].color=="Amarillo"):
                x=jugadores[i].base[0]
                y=jugadores[i].base[1]
                for j in range(0,4):
                    x+=15
                    y+=10
                    button3 = Button(window, text = "" )
                    button3.configure(width = 2, activebackground = "#FDC90D",background="#FDC90D")
                    button3_window = canvas.create_window(x,y, anchor=NW, window=button3)
                    ficha = Ficha([x,y],"Amarillo",[x,y],self.control.tablero.tablero.obtenerNodo((9,13)),button3,button3_window,self.control.tablero.tablero.obtenerNodo((9,13)))
                    jugadores[i].fichas.append(ficha)     
                
            elif(jugadores[i].color=="Verde"):
                x=jugadores[i].base[0]
                y=jugadores[i].base[1]
                for j in range(0,4):
                    x+=15
                    y+=10
                    button4 = Button(window, text = "" )
                    button4.configure(width = 2, activebackground = "#2E933C",background="#2E933C")
                    button4_window = canvas.create_window(x,y, anchor=NW, window=button4)
                    ficha = Ficha([x,y],"Verde",[x,y],self.control.tablero.tablero.obtenerNodo((1,9)),button4,button4_window,self.control.tablero.tablero.obtenerNodo((1,9)))
                    jugadores[i].fichas.append(ficha) 
        
        #Funcion: Configura la funcionalidad de las fichas al ser tocadas
        #Requiere: El canvas donde se colocan las fichas y la lista de jugadores no vacia 
        #Modifica: El boton de cada ficha dentro del juego
        #Retorna: --
    def configurarBotones(self,jugadores,canvas,controlador,lab,lab2,lab3):
        for i in range(0,len(jugadores)):
            if(jugadores[i].color=="Azul"):
                j=i
                jugadores[j].fichas[0].boton.configure(command=lambda:self.moverFicha(jugadores[j].fichas[0].botonVista,canvas,jugadores,j,0,controlador,lab.cget("text"),lab2,lab3))
                jugadores[j].fichas[1].boton.configure(command=lambda:self.moverFicha(jugadores[j].fichas[1].botonVista,canvas,jugadores,j,1,controlador,lab.cget("text"),lab2,lab3))
                jugadores[j].fichas[2].boton.configure(command=lambda:self.moverFicha(jugadores[j].fichas[2].botonVista,canvas,jugadores,j,2,controlador,lab.cget("text"),lab2,lab3))
                jugadores[j].fichas[3].boton.configure(command=lambda:self.moverFicha(jugadores[j].fichas[3].botonVista,canvas,jugadores,j,3,controlador,lab.cget("text"),lab2,lab3))
            
            elif(jugadores[i].color=="Rojo"):
                r=i
                jugadores[r].fichas[0].boton.configure(command=lambda:self.moverFicha(jugadores[r].fichas[0].botonVista,canvas,jugadores,r,0,controlador,lab.cget("text"),lab2,lab3))
                jugadores[r].fichas[1].boton.configure(command=lambda:self.moverFicha(jugadores[r].fichas[1].botonVista,canvas,jugadores,r,1,controlador,lab.cget("text"),lab2,lab3))
                jugadores[r].fichas[2].boton.configure(command=lambda:self.moverFicha(jugadores[r].fichas[2].botonVista,canvas,jugadores,r,2,controlador,lab.cget("text"),lab2,lab3))
                jugadores[r].fichas[3].boton.configure(command=lambda:self.moverFicha(jugadores[r].fichas[3].botonVista,canvas,jugadores,r,3,controlador,lab.cget("text"),lab2,lab3))
            
            elif(jugadores[i].color=="Verde"):
                v=i
                jugadores[v].fichas[0].boton.configure(command=lambda:self.moverFicha(jugadores[v].fichas[0].botonVista,canvas,jugadores,v,0,controlador,lab.cget("text"),lab2,lab3))
                jugadores[v].fichas[1].boton.configure(command=lambda:self.moverFicha(jugadores[v].fichas[1].botonVista,canvas,jugadores,v,1,controlador,lab.cget("text"),lab2,lab3))
                jugadores[v].fichas[2].boton.configure(command=lambda:self.moverFicha(jugadores[v].fichas[2].botonVista,canvas,jugadores,v,2,controlador,lab.cget("text"),lab2,lab3))
                jugadores[v].fichas[3].boton.configure(command=lambda:self.moverFicha(jugadores[v].fichas[3].botonVista,canvas,jugadores,v,3,controlador,lab.cget("text"),lab2,lab3))

            elif(jugadores[i].color=="Amarillo"):
                a=i
                jugadores[a].fichas[0].boton.configure(command=lambda:self.moverFicha(jugadores[a].fichas[0].botonVista,canvas,jugadores,a,0,controlador,lab.cget("text"),lab2,lab3))
                jugadores[a].fichas[1].boton.configure(command=lambda:self.moverFicha(jugadores[a].fichas[1].botonVista,canvas,jugadores,a,1,controlador,lab.cget("text"),lab2,lab3))
                jugadores[a].fichas[2].boton.configure(command=lambda:self.moverFicha(jugadores[a].fichas[2].botonVista,canvas,jugadores,a,2,controlador,lab.cget("text"),lab2,lab3))
                jugadores[a].fichas[3].boton.configure(command=lambda:self.moverFicha(jugadores[a].fichas[3].botonVista,canvas,jugadores,a,3,controlador,lab.cget("text"),lab2,lab3))
                   