'''classe que representa problema do deposito'''

from deposito.encher import Encher
from deposito.vazar import Vazar
from mod.estado import Estado
from mod.problema import Problema


class DepositoAgua(Problema):
    def __init__(self, vol_inicial, vol_final):
        self.vol_inicial = vol_inicial
        self.vol_final = vol_final
        self.estado = Estado()
        super().__init__(self.estado, [Encher(2), Encher(3), Vazar(2), Vazar(3)])
        
    '''estado é objetivo se volume desse estado for igual ao volume final do problema'''
    def objectivo(self, estado):
       return estado.volume == self.vol_final
   
