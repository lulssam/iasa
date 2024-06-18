from ..mec_proc.mecanismo_procura import MecanismoProcura
from .fronteira_lifo import FronteiraLIFO

class ProcuraProfundidade(MecanismoProcura):

    '''
    no construtor vamos invocar a super classe passando a fronteira que queremos
    no caso da procura em profundidade seria a fronteira lifo:
    '''
    def __init__(self):
        super().__init__(FronteiraLIFO())
        
        
    # inserir o nó na fronteira, usa o mecanismo procura
    def _memorizar(self, no):
        self._fronteira.inserir(no)