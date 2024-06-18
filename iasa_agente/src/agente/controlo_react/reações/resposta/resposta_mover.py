'''
Representa a ação, e a ação do movimento na direção indicada no construtor
Extende a classe Resposta que permite a moviementação do agente.
'''

from sae import Accao
from ecr.resposta import Resposta
class RespostaMover(Resposta):
    def __init__(self, direcao):
        accao = Accao(direcao)
        super().__init__(accao)