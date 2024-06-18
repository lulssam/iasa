from mod.estado import Estado
from mod.operador import Operador
from pdm.modelo.modelo_pdm import ModeloPDM
from plan.modelo.modelo_plan import ModeloPlan

'''
Guarda objetivos e resposta máxima
Transições são pre calculadas para maximizar eficicencia
'''

class ModeloPDMPlan(ModeloPDM, ModeloPlan):
    # construtor
    def __init__(self, modelo_plan: ModeloPlan, objetivos, rmax = 1000):
        # guardar arguementos olka
        self.__modelo_plan = modelo_plan
        self.__objectivos = objetivos
        self.__rmax = rmax
        # dicionário para calcular transições, definido por significado. Par estado/ação
        self.__transicoes = {
            # iniciar todas transições possiveis
            (s, a): a.aplicar(s)
            for s in self.obter_estados()
            for a in self.obter_operadores()
        }
    '''
    já existe no modelo plan que é passado
    invocar passando o valor'''
    def obter_estado(self):
        return self.__modelo_plan.obter_estado()   
    
    def obter_estados(self):
        return self.__modelo_plan.obter_estados()
    
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()
   
    def S(self) -> list:
        """Devolve um conjunto de estados. Usar função do ModeloPlan

        Returns:
            list: Lista obter_estados()
        """
        return self.obter_estados()
        
  
    def A(self, estado: Estado):
        """Devolve operadores que não são estados terminais
        Usar operador ternário

        Args:
            estado (Estado): Estado passado

        Returns:
            list: Conjunto de operadores disponivel se o estado não for estado objetivo. Caso contrário, retorna lista vaziz
        """
        return self.obter_operadores() if estado not in self.__objectivos else []
    
    def T(self, estado: Estado, operador: Operador, estado_sucessor: Estado):
        """Se ação poder ser executada, prob = 1 caso contrário = 0
        para ver se transição existe ver se ela está na tabela de transições

        Args:
            estado (Estado): Estado Passado
            operador (Operador): Operador
            estado_sucessor
        """
        return 1 if self.__transicoes.get((estado, operador)) == estado_sucessor else 0
        
    def R(self, estado, operador, estado_sucessor):
        """Se for um objetivo, a recompensa é maximo. Caso contrário é cuso do operador.

        Args:
            estado (Estado)
            operador (Operador)
            estado_sucessor (Estado)

        Returns:
            Retorna a recompensa ou o custo
        """
        return self.__rmax if estado_sucessor in self.__objectivos else -operador.custo(estado, estado_sucessor)
        
    def suc(self, estado: Estado, operador: Operador) -> list:
        """Gere proximos estados par quando estamos a fazer os somatorios
        Sucessor va utilizadr transições já utilizadas
        
        Returns:
            list: Estado sucessor se existir, caso contrário, lista vazia
        """
        estado_sucessor = self.__transicoes.get((estado, operador))
        return [estado_sucessor] if estado_sucessor else []
        