from pdm.mec_util import MecUtil


class PDM():
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max
        self.__mec_util = MecUtil(self.__modelo, self.__gama, self.__delta_max)
     
    # se nos soubermos o estado, diz nos uma ação
    # dicionario onde chave é o estado e o valor uma ação
    # para cada esatdo a melhor ação será a indicada
    def politica(self, U):
        S, A = self.__modelo.S, self.__modelo.A
        
        politica = {}
        
        for s in S():
            if A(s):
                mel_pol = max (A(s), key=lambda a: self.__mec_util.util_acao(s, a, U))
                politica[s] = mel_pol
        return politica
    
    def resolver(self):
        return (self.__mec_util.utilidade(), self.politica(self.__mec_util.utilidade()))
        