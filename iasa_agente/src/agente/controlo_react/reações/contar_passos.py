'''
Por cada passo, conta um passo e mostra a contagem no ecrã. 
Quando chegar a 10 passos, move-se para norte

'''

from agente.controlo_react.reações.resposta.resposta_mover import RespostaMover
from ecr.comportamento import Comportamento
from sae.ambiente.direccao import Direccao

class ContarPassos(Comportamento):
    def __init__(self):
        # Iniciar o contador
        self._passos = 0
        
        # Definir a resposta de mover para norte
        self._resposta = RespostaMover(Direccao.NORTE)
        
    def activar(self, percepcao):
        # Incrementar o contador
        self._passos += 1
        print(self._passos)
        if self._passos >= 10:
            return self._resposta.activar(percepcao)