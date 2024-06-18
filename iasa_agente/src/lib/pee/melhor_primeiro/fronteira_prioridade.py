from heapq import heappush, heappop
from pee.mec_proc.fronteira import Fronteira



class FronteiraPrioridade(Fronteira):
    def __init__(self, avaliador):
        self._avaliador = avaliador
        
    def inserir(self, no):
        prioridade = self._avaliador.prioridade(no)
        heappush(self._nos, (prioridade, no))
        
    def remover(self):
        _, no = heappop(self._nos)
        return no