from random import choice
from agente.controlo_react.reações.resposta.resposta_mover import RespostaMover
from sae.ambiente.direccao import Direccao


class RespostaEvitar(RespostaMover):
    def __init__(self, dir_inicial=Direccao.ESTE):
        super().__init__(dir_inicial)
        self._direccoes = list(Direccao)
    
    def activar(self, percepcao, intensidade=0):         
        # Código redundante
        # if percepcao.contacto_obst(self._accao.direccao):
        #     direccao_livre = self._direccao_livre(percepcao)
        #     if direccao_livre:
        #         self._accao.direccao = direccao_livre
        #         return super().activar(percepcao, intensidade)
        #     else:
        #         return None
        # else:
        #     super().activar(percepcao, intensidade)
            
        # Codigo com elses por omissão para ficar menos redundante
        if percepcao.contacto_obst(self._accao.direccao):
            direccao_livre = self._direccao_livre(percepcao)
            if direccao_livre:
                self._accao.direccao = direccao_livre
            else:
                return None
        
        return super().activar(percepcao, intensidade)
    
    # Para cada uma das direções possiveis, se em nenhuma delas há obstáculo, é uma  direção livre
    def _direccao_livre(self,percepcao):
        dir_livre = [direccao for direccao in  self._direccoes if not percepcao.contacto_obst(direccao)]
        return choice(dir_livre)
        