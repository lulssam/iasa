'''
Modelarizar o processo deliberação do processo computacional.
Como existe alguma complexidade neste processo, colocamos em
evidencia que implementa este mecanismo.
Não faz parte do modelo do mundo, usa o modelo. Faz é parte do agente.
'''


from sae.ambiente.elemento import Elemento


class MecDelib:
    # Guardar o modelo do mundo
    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo
        
    # Vai dar forma a raciocinio.
    # Vamos primeiro gerar uma lista de objetivos que são 
    # estados em que o elemento da posição corrente são estados. 
    # Ver as posições cujo o elemento que la está é o alvo
    # Retorna uma lista de objetivos   
    # Tem acesso ao modelo do mundo que da info sobre todos os estados e 
    # depois para cada estado da info do elemento que la está.
    def deliberar(self):
        # objetivos = []
        # estados = self.__modelo_mundo.__estados
        # for estado in estados:
        #     elemento = self.__modelo_mundo.obter_elementos(estado)
        #     if elemento is self.__modelo_mundo.elementos.ALVO:
        #         objetivos.append(elemento)
        # return objetivos
        
        # codigo mais completo
        # objetivos =  para cada estado nos estados
        objetivos = [estado for estado in self.__modelo_mundo.obter_estados()
                     # se o estado for um alvo
                     if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]
        # se houverem objetivos
        if objetivos:
            # organizar lista por distância usando a chave do modelo mundo
            objetivos.sort(key=self.__modelo_mundo.distancia)
            return objetivos