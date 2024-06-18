from pee.melhor_primeiro.aval.aval_heur import AvaliadorHeur

# Estende a classe AvaliadorHeur
class AvaliadorSof(AvaliadorHeur):
    # construtor
    def __init__(self):
        #super().__init__()
        ''''''
     
    # recebe um no e retorna um double   
    def prioridade(self, no):
        return self._heuristica.h(no.estado)