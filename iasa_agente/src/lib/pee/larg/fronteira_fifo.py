from pee.mec_proc.fronteira import Fronteira

'''
FIFO -> first in first out. Os mais antigos são os que vão
sair primeiro.
Usado na procura em largura.
'''

class FronteiraFIFO(Fronteira):
    def __init__(self, no):
        self._nos.insert(no)
        super().__init__()
        
    def inserir(self, no):
        return self._nos.insert(0, no)