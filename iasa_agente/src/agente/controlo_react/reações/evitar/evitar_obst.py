'''
Evitar o alvo do objeto
'''

from agente.controlo_react.reações.evitar.evitar_dir import EvitarDir
from agente.controlo_react.reações.evitar.resposta_evitar import RespostaEvitar
from ecr.hierarquia import Hierarquia
from sae.ambiente.direccao import Direccao


class EvitarObst(Hierarquia):
    
    # construtor
    def __init__(self):
        self.__resposta_evitar = RespostaEvitar()
        # lista dos comportamentos
        comportamentos = [EvitarDir(direccao, self.__resposta_evitar) for direccao in Direccao]
        # super classe hierarquia com a lista
        super().__init__(comportamentos)
        