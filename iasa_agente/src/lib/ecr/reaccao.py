# Implementação do mecanismo base de uma reação.
# Uma reação associa estímulas a respostas
# Resposta funciona como encapsulador de ação. Também tem uma ação associada.

from .comportamento import Comportamento

class Reaccao(Comportamento):
    def __init__(self, estimulo, resposta):
        self.__estimulo = estimulo
        self.__resposta = resposta

    def activar(self, percepcao):
        intensidade = self.__estimulo.detectar(percepcao)
        
        if intensidade > 0:
            accao = self.__resposta.activar(percepcao, intensidade)
            return accao
        
        