from abc import ABC, abstractmethod


class Fronteira(ABC):
    
    '''
    iniciar a estrutura de nós com uma lista vazia
    '''
    def __init__(self): 
        # redundante -> chamamos o inicar no construtor
        # self.nos = []
        self.iniciar()
    
    def iniciar(self):
        self._nos = []
    
    @abstractmethod
    def inserir(self, no):
        raise NotImplementedError
    
    
    '''
    Remover o primeiro usando o método pop
    '''
    def remover(self):
        if (self._nos is not None):
             return self._nos.pop(0)
        else:
            return None
       
    
    @property
    def vazia(self):
        '''
        Propriedade derivada dos nós
        Nas propriedades derivadas, o valor retornado não
        depende de um valor interno
        retornar um boleano que indica que os nos não tem nenhum array
        o seu valor é derviado em tempo de execução de outro objeto
        '''
        return len(self._nos) == 0
    
    @property
    def dimensao(self):
        '''
        dimensao da fronteira
        retorna a dimensão da lista de nos
        retorna o número de nos.
        '''
        if self._nos is not None:
            return len(self._nos)
        return None