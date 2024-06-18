'''
Estados representão situações possíveis de um problema.
Tem uma identificação unica.
Um espaço de estados -> conjunto de estados e de transições de estado
'''
from abc import ABC, abstractmethod

class Estado(ABC):
    
    @abstractmethod
    def id_valor(self):
        ''''''
    def __hash__(self):
        return self.id_valor()
    # operador de igualdade -> == corresponde ao .equals() em JAVA
    def __eq__(self, other):
        # o outro objeto também tem de ser um estado, tem de ser do mesmo tipo e ter o mesmo tipo.
        if isinstance(other, Estado):
            # return self.id_valor() = other.id_valor() também seria valido.
            # usamos o hash so para ser tudo consistente
            return self.__hash__() == other.__hash__()