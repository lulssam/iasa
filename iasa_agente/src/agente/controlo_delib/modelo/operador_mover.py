import math
from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from mod.operador import Operador
from sae.agente.accao import Accao

'''
Implementa a interface Operador
'''
class OperadorMover(Operador):
    
    def __init__(self, modelo_mundo, direccao):
        self.__modelo_mundo = modelo_mundo
        self.__direccao = direccao
        self.__accao = Accao(self.__direccao)
        
    # propridede read only
    @property
    def ang(self):
        return self.__accao.direccao.value
    
    # propridede read only
    @property
    def accao(self):
        return self.__accao
    
    # Construtor da classe
     
    # Onde é simulada a ação   
    def aplicar(self, estado):
        # Obter o angulo
        ang = self.__accao.direccao.value
        # Obter o passo
        passo = self.__accao.passo
        # Calculo para dx
        dx = passo * math.cos(ang)
        # Calculo para dy, ao contrário de na vida real, aqui y vai de cima para baixo
        dy = -1 * math.sin(ang)
        # arredondar numeros para garantir precisão
        posicao = round(estado.posicao[0] + dx), round(estado.posicao[1] + dy)
        # criar novo estado sucessor com nova posicão
        estado_suc = EstadoAgente(posicao)
    
    def custo(estado, estado_suc):
        return math.dist(estado.posicao, estado_suc.posicao)
    
    