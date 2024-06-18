# Import para fazer interface
from abc import ABC, abstractmethod

'''
Interface
'''

class Planeador(ABC):
    @abstractmethod
    # tipo plano
    def planear(self, modelo_plan, objetivos):
        '''...'''