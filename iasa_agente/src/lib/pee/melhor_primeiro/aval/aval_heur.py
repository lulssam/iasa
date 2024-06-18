from pee.melhor_primeiro.aval.heuristica import Heuristica


# Estende a interface Heuristica
class AvaliadorHeur(Heuristica):
    
    # constutor
    def __init__(self, heuristica):
        self._heuristica = heuristica