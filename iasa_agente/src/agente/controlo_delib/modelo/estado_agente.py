from mod.estado import Estado


class EstadoAgente(Estado):
    # Construtor da classe
    def __init__(self, posicao):
        self.__posicao = posicao

    @property
    def posicao(self):
        return self.__posicao
            
    # Método da classe super
    def id_valor(self):
        return hash(self.__posicao)