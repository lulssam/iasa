from pee.melhor_primeiro.aval.aval_custo_unif import AvaliadorCustoUnif
from pee.melhor_primeiro.procura_melhor_prim import ProcuraMelhorPrim

# Estende classe ProcuraMelhorPrim
class ProcuraCustounif(ProcuraMelhorPrim):
    def __init__(self):
      super().__init__(AvaliadorCustoUnif())