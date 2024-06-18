'''
Gerar uma reação para evitar numa dada direção
'''
from agente.controlo_react.reações.evitar.estimulo_obst import EstimuloObst
from ecr.reaccao import Reaccao


class EvitarDir(Reaccao):
    
    # construtor
    def __init__(self, direccao, respostaEvitar):
        """Construtor

        Args:
            direccao: Direção a seguir para evitar
            respostaEvitar: Reação
        """
        estimulo = EstimuloObst(direccao)
        super().__init__(estimulo, respostaEvitar)