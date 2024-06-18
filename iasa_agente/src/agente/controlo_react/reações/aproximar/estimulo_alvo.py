from ecr.estimulo import Estimulo
from sae.ambiente.elemento import Elemento

class EstimuloAlvo(Estimulo):
    def __init__(self, direccao, gama=0.9):
        self.__gama = gama
        self.__direccao = direccao
    
    def detectar(self, percepcao):
        elemento, distancia, _ = percepcao[self.__direccao]
        # se elemento é um alvo
        if elemento == Elemento.ALVO:
            # true -> atribuir intensidade valor gama elevada a distancia
            intensidade = self.__gama ** distancia 
        else:
            # false -> intensidade = 0
            intensidade = 0
        return intensidade
        
        