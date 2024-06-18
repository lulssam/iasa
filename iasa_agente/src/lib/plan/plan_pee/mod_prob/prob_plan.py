from mod.problema import Problema

'''
estado é objetivo quando estado é igual ao estado final
'''
class ProblemaPlan(Problema):
    # construtor
    def __init__(self, modelo_plan ,estado_final):
        self.modelo_plan = modelo_plan
        self.__estado_final = estado_final
        estado_inicial = self.modelo_plan.obter_estado()
        operadores = self.modelo_plan.obter_operadores()
        # ativar construtor da super classe
        super().__init__(estado_inicial, operadores)
    
    # método booleano que verifica se estado é objetivo
    def objectivo(self, estado):
        # se estado é igual ao estado final
        if estado == self.__estado_final:
            # é objetivo
            return True
        return False