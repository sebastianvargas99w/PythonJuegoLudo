
#Se encarga de asegurarse de que las reglas se cumplan
class I_Arbitro(Interface):


    #Función: Indica si se puede hacer algun movimiento
    #Requiere: tablero cleado, una posicion en el tablero y fichas inicializadas
    #Modifica: No modifica ningun parametro
    #Retorna: si le movimiento es valido
    @abstractmethod
    def movimientoValido(self,tablero,ficha,posicion=None):
        pass
    
    #Función: Indica el ganador de la partida
    #Requiere: tablero cleado y que contenga fichas
    #Modifica: No modifica ningun parametro
    #Retorna: si hay ganado retorna el color

    @abstractmethod
    def ganadorPartida(self,tablero):
        pass

    #Función: termina el turno
    #Requiere: el juego iniciado 
    #Modifica: Turno actual
    #Retorna: no retorna ningun parametro
    @abstractmethod
    def terminarTurno(self,controlador):
        pass
    

