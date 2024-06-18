from pee.mec_proc.procura_grafo import ProcuraGarfo

'''
a procura em largura é uma procura garfo que
utiliza uma fronteira do tipo FIFO
-Critério de exploração: menor profundidade
'''
class ProcuraLargura(ProcuraGarfo):
    def __init__(self, fronteira_fifo):
        super().__init__(fronteira_fifo)
        
    
        
        