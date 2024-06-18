'''
se o operador incrementa, implementa a interface operador
este operador incremente não depende do estado nem do esatdo anterior

return self.__incremento ** 2
'''

from contagem.mod_prob.estado_contagem import EstadoContagem
from lib.mod.operador import Operador

class OperadorIncremento(Operador):
    
    def __init__(self, incremento):
        self._incremento = incremento
    
    # transforma um estado num novo estado efetuando sobre esse estado 
    def aplicar(self, estado):
        return EstadoContagem(estado.id_valor() + self._incremento)
    
    def custo(self, estado, estado_suc):
        return self._incremento ** 2
    
    