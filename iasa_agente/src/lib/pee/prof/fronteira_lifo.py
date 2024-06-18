from pee.mec_proc.fronteira import Fronteira

'''
Fronteira LIFO -> Last in first out. Logo os mais novos são os primeiros a sair
Na procura em largura utiliza uma fronteira lifo
'''

class FronteiraLIFO(Fronteira):
    
    def __init__(self):
        super().__init__()
        
    def inserir(self, no):
        # fazemos append pois o ultimo a entrar é o primeiro a sair
        self._nos.append(no)
    