from abc import ABC, abstractmethod

class ModeloPDM(ABC):
    # S é o conjento de estados no mundo
    @abstractmethod
    def S(self):
        ''''''
    
    # Método que representa o conjunto de ações posssiveis no estado
    # para todo s pertence a S
    @abstractmethod
    def A(self, s):
        ''''''
        
    # Método que representa a probabilidade de transição de s para s' através de a
    @abstractmethod     
    def T(self, s, a, sn):
        ''''''
        
    # método resposavel pela recompesa esperada na transição de s para s'
    # através de a
    @abstractmethod
    def R(self, s, a, sn):
        ''''''
        
    @abstractmethod
    def suc(self, s, a):
        ''''''