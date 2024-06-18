from pee.melhor_primeiro.aval.aval_heur import AvaliadorHeur


class AvaliadorAA(AvaliadorHeur):
    # construtor
    def __init__(self):
        super().__init__()
    
    # recebe um no e retorna um double
    def prioridade(self, no):
        return no.custo + self._heuristica.h(no.estado) # custo uniforme -> custo do nó  + heuristica do estado do nó