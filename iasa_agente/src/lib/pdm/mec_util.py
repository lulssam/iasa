from pdm.modelo.modelo_pdm import ModeloPDM


class MecUtil():
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max
        
        #self.__modelo = ModeloPDM()
    
    @property
    def delta_max(self):
        return self.__delta_max
    
    @property
    def gama(self): 
        return self.__gama
    
    def utilidade(self):
        
        # U = {s: 0 for s in self.__modelo.S()}
        # Uant = U.copy()
        # self.delta = 0
        # while self.delta > self.__delta_max:
        #     Uant = U.copy()
        #     self.delta = 0
        #     for s in self.__modelo.S():
        #         U[s] = max(self.util_acao(s, (a for a in self.__modelo.A()), Uant))
        #         if self.delta > max(abs(U[s] - Uant[s])): 
        #             self.delta = max(self.delta, abs(U[s] - Uant[s]))
        # return U
        
        S, A = self.__modelo.S, self.__modelo.A
        U = {s: 0.0 for s in S()}
        while True:
            Uant = U.copy()
            delta = 0
            for s in S():
                #print(self.util_acao(s, '<', Uant))
                #print(self.util_acao(s, '>', Uant))
                U[s] = max([self.util_acao(s, a, Uant) for a in A(s)], default=0)
                delta = max(delta, abs(U[s] - Uant[s]))
            if delta <= self.__delta_max:
                break
        return U
                
    
    # método implementa a função utilidade ação. A utilidade realiza uma ação de um estado
    # o somatorio diz a utilidade do estado s realizado uma ação a
    def util_acao(self, s, a, U):
        # prob = 0
        # for suc in self.__modelo.suc(s, a):
        #     prob += (self.__modelo.T(s, a, suc) * (self.__modelo.R(s, a, suc) + self.__gama * U[suc]))  
        T, R, suc = self.__modelo.T, self.__modelo.R, self.__modelo.suc
        return sum(T(s,a,sn)*(R(s,a,sn) + self.__gama * U[sn]) for sn in suc(s,a))
    
