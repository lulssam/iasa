from plan.plano import Plano

class PlanoPDM(Plano):
    '''politica diz para cada estado qual é a ação'''
    def __init__(self, utilidade, politica):
        """Construtor para guardar parametros

        Args:
            utilidade,
            politica
        """
        self.__utilidade = utilidade
        self.__politica = politica
        
    def obter_accao(self, estado):
        """Aceder a politica se existir politica,
        retorna a politica para o estado indicado

        Args:
            estado (Estado): Estado

        Returns:
            Operador
        """
        if self.__politica:
            return self.__politica.get(estado)
        
    def mostrar(self, vista):
        # se existe politica, também existe utilidade
        if self.__politica:
            # para cada valor na utilidade
            for estado, valor in self.__utilidade.items():
                # mostrar codigo de cores
                vista.mostrar_valor_posicao(estado.posicao, valor) # método da SAE
            # para cada estado da ação na politica
            for estado, accao in self.__politica.items():
                # mostrar a ação com o vetor
                vista.mostrar_vector(estado.posicao, accao.ang) # método da SAE
                
    @property
    def politica(self):
        return self.__politica
    
    @property
    def utilidade(self):
        return self.__utilidade