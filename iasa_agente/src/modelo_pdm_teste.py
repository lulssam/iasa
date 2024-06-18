'''
instanciar modelo
instanciar pdm com o modelo
usar o metodo resolver

'''

from pdm.modelo.modelo_pdm import ModeloPDM
from pdm.pdm import PDM


class ModeloPDMTeste(ModeloPDM):
    
    # def __init__(self) -> None:
    #     gama = 0.5
    #     delta_max = 0.0
    #     modelo_pdm = ModeloPDM(gama, delta_max)
    #     pdm = PDM(modelo_pdm, gama, delta_max)
    #     utilidade, politica = pdm.resolver()
    
    def S(self) -> list:
        """
        define modelo do mundo
        Returns:
            list: modelo do mundo
        """
        # acrescentado desde ultima entrega
        # retorna 
        return [1,2,3,4,5,6,7]
        
    def A(self, s):
        """
        define conjunto de ações para cada estado -> A(s)

        Args:
            estado (estado): estado

        Returns:
            list: lista de operadores
        """
        return ['<', '>'] if s not in [1, 7] else[]      
    
    def T(self, s):
        """
        Modelo de transição. Tem uma probabilidade.
        Indica para ação, estado e estado possivel qual a probabilidade

        Args:
            s (estado)
        Returns:
            double
        """
        return 1 if s not in [1, 7] else 0
        
    def R(self, s):
        """Modelo de recompensa.
        Só nos terminais é que não conta

        Args:
            estado (estado):

        Returns:
            double:
        """
        return 1 if s == 7 else -1 if s == 1 else 0
        
    def suc(self, s, a) -> list:
        """

        Args:
            s (estado): estado
            a (accao): accao

        Returns:
            list
        """
        return [max(1, s-1) if a == '<' else min(7, s + 1)]
        