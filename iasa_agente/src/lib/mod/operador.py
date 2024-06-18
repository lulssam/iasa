from abc import ABC, abstractmethod

'''
Operadores representão ações que produzem transições de estado.

'''
class Operador(ABC):
    @abstractmethod
    def aplicar(self, estado):
        raise NotImplementedError
    
    @abstractmethod
    def custo(self, estado, estado_suc):
        raise NotImplementedError

