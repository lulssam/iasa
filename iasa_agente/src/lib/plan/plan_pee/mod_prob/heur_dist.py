import math
from pee.melhor_primeiro.aval.heuristica import Heuristica

'''
calcula distancia entre heuristica deste estado passado e o estado final
diz-se que heurisitica é um método de procura baseado na aproximação progressiva de um certo problema
'''

class HeurDist(Heuristica):
    # construtor
    def __init__(self, estado_final):
        self.__estado_final = estado_final
    
    # representa função heuristica
    # retorna posição referente ao estado e a posição do estado final
    def h(self, estado):
        return math.dist(estado.posicao, self.__estado_final.posicao)