from contagem.mod_prob.estado_contagem import EstadoContagem
from contagem.mod_prob.operador_incremento import OperadorIncremento
from mod.problema import Problema


class ProblemaContagem(Problema):
    def __init__(self, valor_inicial, valor_final, incrementos):
        super().__init__(EstadoContagem(valor_inicial), 
                                        [OperadorIncremento(incremento) 
                                         for incremento in incrementos])
        self.__valor_final = valor_final
        
    '''
    retornar valor do estado se for maior ou igual ao valor final
    metodo que diz quando é que o estado é objetivos
    '''
    
    def objectivo(self, estado):
        return estado.id_valor() >= self.__valor_final