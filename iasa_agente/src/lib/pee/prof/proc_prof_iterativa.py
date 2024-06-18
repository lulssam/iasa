'''
utiliza a profundidade iterativa com limites de profundidade crescentes
não é mantida memória de nós explorados entre procuras
    - mantém as caracteristicas de complexidade da procura em profundidade
    - possibilidade de limitar a procura a uma profundidade maxima
    
processo de procura:
    - para um limte de profundidade crescente
        - realizar uma procura em profundidade com o limite de profundidade actual
        
'''

from pee.prof.proc_prof_lim import ProcuraProfLim


class ProcuraProfIter(ProcuraProfLim):
    
    '''
    Para um limite de profundidade crescente
        * realizar uma procura em profundidade com o limite de profundidade atual
        * se existe solução, retorna-la
    '''
    def procurar(self, problema, inc_prof, limite_prof = 1000):
        # percorrer desde 0 até 1000, usamos + 1 pois range para um indice antes
        for profundidade in range(0, limite_prof + 1, inc_prof):
            # atribuir nova profundidade maxima
            self.prof_max = profundidade
            # procurar solução do problema
            solucao = super().procurar(problema)
            # se houver solução
            if solucao:
                #retorna-la
                return solucao
            
            
        
    