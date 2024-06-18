from pee.melhor_primeiro.aval.aval_sof import AvaliadorSof
from pee.melhor_primeiro.procura_informada import ProcuraInformada

# Estende a classe ProcuraInformada
class ProcuraSofrega(ProcuraInformada):
    
    # construtor
    def __init__(self):
        super().__init__(AvaliadorSof())