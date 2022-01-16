from abc import ABC, abstractmethod
from interface import implements, Interface
class I_Grafico(Interface):
    
    #Funcion: Limpia los datos ingresados en la pantalla del menu principal lo que permite ingresar nuevos datos
    #Requiere: Lista de jugadores no vacia y una instancia de controlador para reiniciar la lista.
    #Modifica: La lista de jugadores y los aspectos graficos de entrada de datos.
    #Retorna: --
    @abstractmethod
    def resetMenu(self,jugadores,controlador):
        pass

    #Funcion: Carga en pantalla la ventana principal con el juego.
    #Requiere: La ventana del menu desde donde se carga la nueva pantalla y lista de jugadores no vacia.
    #Modifica: La ventana del menu se oculta.
    #Retorna: --
    @abstractmethod
    def cargarTablero(self,ventanaMenu,controlador,jugadores):
        pass

    #Funcion: Elimina la ventana del juego actual y regresa el jugador a la ventana del menu principal
    #Requiere: La ventana actual del juego que se va eliminar y la ventana del menu principal que cargo la ventana del juego además de lista de jugadores no vacia 
    #Modifica: Ventana actual
    #Retorna: --
    @abstractmethod
    def resetVenJu(self,windows,ventanaMenu,jugadores,controlador):
        pass

    #Funcion: Carga una nueva partida previamente guardada 
    #Requiere: Estar en la ventana del juego y tener un archivo valido para cargarlo
    #Modifica: La partida actual se sobreescribe 
    #Retorna: --
    @abstractmethod
    def cargar(self,window,controlador,jugadores):
        pass

    #Funcion: Guarda la partida actual 
    #Requiere: Estar en la ventana del juego.
    #Modifica: --
    #Retorna: Genera un archivo con la partida guardada
    @abstractmethod
    def guardar(self,window,controlador):
        pass

    #Funcion: Pasa el turno al siguiente jugador
    #Requiere: Lista de jugadores no vacia y una etiqueta para colocar el color del siguiente jugador
    #Modifica: La etiqueta
    #Retorna: --
    @abstractmethod
    def cambiarTurnos(self,label,controlador,jugadores):
        pass

    #Funcion: Es la ventana del menu principal desde donde se ingresan los datos del juego
    #Requiere: --
    #Modifica: Añade los jugadores a la lista de jugadores y les asigna el color segun los datos ingresados
    #Retorna: --
    @abstractmethod
    def ventanaMenu(self,jugadores,controlador):
        pass

    #Funcion: Es la ventana principal del juego donde esta el tablero y los demás elementos 
    #Requiere: Lista de jugadores no vacia 
    #Modifica: --
    #Retorna: --
    @abstractmethod
    def ventana(self,jugadores,controlador,venMenu):
        pass

    #Funcion: Muestra el las reglas del juego y las instrucciones generales 
    #Requiere: Una instancia de ayuda
    #Modifica: --
    #Retorna: --
    @abstractmethod
    def manual(self):
        pass