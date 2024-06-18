from pee.melhor_primeiro.aval.aval_aa import AvaliadorAA
from pee.melhor_primeiro.procura_informada import ProcuraInformada

# Estende a classe ProcuraInformada
class ProcuraAA(ProcuraInformada):
    def __init__(self):
        # chama o super
        super().__init__(AvaliadorAA())