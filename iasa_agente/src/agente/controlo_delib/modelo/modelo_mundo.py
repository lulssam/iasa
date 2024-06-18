# Imports
import math
from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from agente.controlo_delib.modelo.operador_mover import OperadorMover
from mod.operador import Operador
from plan.modelo.modelo_plan import ModeloPlan
from sae.agente.controlo import Controlo
from sae.ambiente.direccao import Direccao
from sae.ambiente.elemento import Elemento

'''
Utiliza operadores que seguem e implementam a interface operador
Mantéma  info se foi alterada ou não
Permite obter o estado atual do agente
Implementa interface Modelo Planeamento
'''

class ModeloMundo(ModeloPlan):
    # Construtor da classe
    def __init__(self):
        self.__estado = None
        self.__estados = []
        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]
        self.__elementos = {}
        self.__recolha = False
        
    
    @property
    def elementos(self):
        return self.__elementos
        
    # Retorna instância de estado do agente
    def obter_estado(self):
        return self.__estado
        
    # Retorna lista de estados do agente para as várias posições que o agente observou.
    # Conjunyo de estados do mundo, elemento do mundo
    def obter_estados(self):
        return self.__estados
    # Percepção tem um atributo elementos
    def obter_elemento(self, estado_agente):
        # posicao = self.__estado_.posicao
        # elemento = self.elementos[posicao]
        # return elemento
        
        # codigo menos redundante
        return self.__elementos.get(estado_agente.posicao)
    

    # Retorna a lista de operadores
    def obter_operadores(self):
        return self.__operadores
        
    # Função dist do mat que retorna a distancia euclideana. 
    # Calcula uma distância no mundo onde o agente está definido
    def distancia(self, estado):
        return math.dist(estado.posicao, self.__estado.posicao)
        
    # Segue a percepção. A percepção tem um atributo posição.
    # Guardar as informações. Atualiza o modelo com base numa perceção.
    def actualizar(self, percepcao):
        self.__elementos = percepcao.elementos
        self.__recolha = percepcao.recolha
        self.__estado = EstadoAgente(percepcao.posicao)
        self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]       
      
    # método auxiliar  
    def mostrar(self, vista):
        for posicao, elemento in self.__elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
        vista.marcar_posicao(self.__estado.posicao)
       
    # propriedade read only
    @property  
    def alterado(self):
        return self.__recolha