'''
Um problema é composto por um estado inicial, operadores e objetivos.

'''

from abc import ABC, abstractmethod

class Problema(ABC):
    def __init__(self, estado_inicial, operadores):
        self.__operadores = operadores
        self.__estado_inical = estado_inicial
        
    @abstractmethod
    def objectivo(self, estado):
        '''raise NotImplementedError'''
      
      
    # Getters em python, usamos a anotação @property. Não precisamos de abrir e fechar()
    @property
    def estado_inicial(self):
        return self.__estado_inical
    
    @property
    def operadores(self):
        return self.__operadoresto 