from pee.mec_proc.passo_solucao import PassoSolucao

'''
Classe que vai criar uma lista de nos com o caminho para a solução
'''

class Solucao():
    def __init__(self, no_final):
        self._no_final = no_final
        self.__passos = []
        no = no_final   
             
        while no.antecedor:
            # criamos um passo 
            passo = PassoSolucao(no.antecedor.estado, no.operador)
            # inserir passo no primeiro indicie da lista 
            self.__passos.insert(0, passo)
            # atribuir no ao no
            no = no.antecedor
        
    # propriedade que retorna a dimensão
    @property
    def dimensao(self):
        return len(self._percurso)
    
    # propriedade que retorna o custo
    @property
    def custo(self):
        return self.custo
    
    # função iteradora que retorna os passos
    # podemos participar num for
    def __iter__(self):
        return iter(self.__passos)
    
    # metodo chamado para tornar classe indexavel
    def __getitem__(self, i):
        return self.__passos[i]
    
    