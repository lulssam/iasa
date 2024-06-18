from pee.melhor_primeiro.aval.heuristica import Heuristica


class HeuristicaContagem(Heuristica):
    def __init__(self, valor_final = 9):
        self.__valor_final = valor_final
        
    def h(self, estado):
        return abs(self.__valor_final - estado.id_valor())