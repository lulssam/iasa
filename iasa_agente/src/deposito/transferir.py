from abc import ABC, abstractmethod


class Transferir(ABC):
    
    def __init__(self, volume):
        # guarda o volume de transferencia
        self.volume = volume
        
    @abstractmethod
    def aplicar(self):
        ''''''
        
    ''' custo é diferença do volume do estado sucessor e o volumo do estado'''
    def custo(self, s, sn):
         return abs(self.volume.custo(sn) - self.volume.custo(s)) ** 2