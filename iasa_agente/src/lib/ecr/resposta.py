# Implementação do mecanismo base de uma resposta.

class Resposta:
    def __init__(self, accao):
        self._accao = accao

    def activar(self, percepcao, intensidade = 0): # podemos invocar este método sem aplicar a intensidade
        self._accao.prioridade = intensidade
        return self._accao