from pee.prof.procura_profundidade import ProcuraProfundidade

'''
Limira a procura a uma profundidade máxima
'''

class ProcuraProfLim(ProcuraProfundidade):
    
    def __init__(self, prof_max):
        super().__init__()
        self.__prof_max = prof_max
    
    
    # só vamos expandir se a profundidade do nó for menor do que a prof max
    def expandir(self, problema, no):
        # criar lista se fronteira for fazia
        fronteira = []
        # se a profundidade for menor do que a profundidade maxima
        if (no.profundidade < self.__prof_max):
            # para cada nó sucessor
           for no.sucessor in self._expandir(problema, no):
               # inserir na fronteira
               fronteira.inserir(no)
               return fronteira
    @property
    def prof_max(self):
        return self.__prof_max
        
    # setter
    @prof_max.setter
    def prof_max(self,valor):
        self.__prof_max = valor