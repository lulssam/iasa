# from abc import ABC, abstractmethod

# from mod.estado import Estado
# '''
# Info do estado atual do sistema
# conjunto de estados validos
# e conjunto de operadores
# '''
# def ModeloPlan(ABC):
#     # tipo estado
#     @abstractmethod
#     def obter_estado():
#         raise NotImplementedError
        
#     # tipo List<Estado>
#     @abstractmethod
#     def obter_estados():
#         raise NotImplementedError
        
#     @abstractmethod
#     # tipo List<Operador>
#     def obter_operadores():
#         raise NotImplementedError

from abc import ABC, abstractmethod

'''
Info do estado atual do sistema
conjunto de estados validos
e conjunto de operadores

Interface
'''
class ModeloPlan(ABC):
    # tipo estado
    @abstractmethod
    def obter_estado(self):
        ''''''
        
    # tipo List<Estado>
    @abstractmethod
    def obter_estados(self):
        ''''''
        
    @abstractmethod
    # tipo List<Operador>
    def obter_operadores(self):
        ''''''
