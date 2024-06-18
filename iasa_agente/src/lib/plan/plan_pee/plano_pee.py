from plan.plano import Plano

'''
forma de ter aceder de uma forma mais simples à solução
'''
class PlanoPEE(Plano):
    def __init__(self, solucao):
        self.__passos = [passo for passo in solucao]
        
    # obter um operador
    def obter_accao(self, estado):
        # verificar se existe passo no plano
        if self.__passos:
            # return primeiro elemento da lista
            passo = self.__passos.pop(0)
            # se passo for igual ao estado
            if passo.estado == estado:
                # return operador
                return passo.operador
        
    def mostrar(self, vista):
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)