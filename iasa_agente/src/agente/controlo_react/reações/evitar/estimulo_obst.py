from ecr.estimulo import Estimulo
from sae.ambiente.elemento import Elemento


class EstimuloObst(Estimulo):
    def __init__(self,direccao, intensidade = 1):
        self.__intensidade = intensidade
        self.__direccao = direccao
    
    def detectar(self, percepcao):
        # '''
        # Se houver contacto com obstaculo, retorna intensidade do construtor,
        # si não retorna 0
        # usar método contacto obs
        # '''
        # if percepcao.contacto_obs(self._direccao):
        #     return self._intensidade
        # else:
        #     return 0
            elemento, distancia, _ = percepcao[self.__direccao]
            if elemento is Elemento.OBSTACULO:
                return self.__intensidade
            return 0
        