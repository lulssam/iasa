'''
A reação do construtor ja recebe um estimulo que recebe uma resposta...
É uma reação.
Modulo que associa a um estimulo alvo uma resposta mover.
'''

from agente.controlo_react.reações.aproximar.estimulo_alvo import EstimuloAlvo
from agente.controlo_react.reações.resposta.resposta_mover import RespostaMover
from lib.ecr.reaccao import Reaccao

class AproximarDir(Reaccao):
    def __init__(self, direccao):
        estimulo = EstimuloAlvo(direccao)
        resposta = RespostaMover(direccao)
        super().__init__(estimulo, resposta)