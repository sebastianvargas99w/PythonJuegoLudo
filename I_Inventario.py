from abc import ABC, abstractmethod
from interface import implements, Interface
class I_Inventario(Interface):
	
	#Funcion: Agrega nuevos elementos a la estructura que se define como almacenador  
    #Requiere: El elemento que se desea agregar
    #Modifica: La estructura de almacenamiento
    #Retorna: --
	@abstractmethod
	def agregar(self,elementoNuevo):
		pass

	#Funcion: Elimina elementos existentes en la estructura que se define como almacenador.
    #Requiere: El elemento que se desea eliminar.
    #Modifica: La estructura de almacenamiento.
    #Retorna: --
	@abstractmethod
	def quitar(self,elementoEliminar):
		pass

	#Funcion: Busca un elemento en La estructura de almacenamiento.
    #Requiere: El elemento que se desea buscar.
    #Modifica: --
    #Retorna: La posicion del elemento si esta, sino retorna -1.
	@abstractmethod
	def esta(self,elemento):
		pass