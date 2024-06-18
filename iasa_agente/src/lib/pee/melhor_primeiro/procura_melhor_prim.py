'''
procura melhor primeira -> avalia os percursos com funçao de avalicação dos nós.
funçao f que normalmente é uma função de custo, tem um valor 0 ou >. Ao seja
quanto maior a função, pior a solução.
então tendo esta função de avaliação, preciso de ordenar os nos da fronteira
por funcao de avaliação. Os que ficam no inicio são os melhores e vao ser os primeiros
a serem explorados
quando ele alguma vez encontrar uma solução vai ser a melhor de todas
'''

from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.mec_proc.no import No
from pee.mec_proc.procura_grafo import ProcuraGarfo
from pee.mec_proc.solucao import Solucao
from pee.melhor_primeiro.fronteira_prioridade import FronteiraPrioridade


class ProcuraMelhorPrim(ProcuraGarfo):
    def __init__(self, fronteira):
        super().__init__(fronteira)
        
    def _manter(self, no, problema):
        # criar nó inicial
        no = No(problema.estado_inicial())
        # iniciar fronteira com prioridade
        fronteira = FronteiraPrioridade(no)
        # iniciar explorados
        explorados = {no.estado : no}
        # enquanto fronteira não for vazia
        while not fronteira.vazia:
            # remover primeiro nó da fronteira
            no = fronteira.remover()
            # verificar se estado do nó é objectivo
            if problema.objectivo(no.estado):
                return Solucao(no)
            # para cada nó sucessor
            for no_sucessor in self._expandir(problema, no):
                super()._manter(no, problema)
            # caso fronteira for vazia, indicar que não existe solução
            return None